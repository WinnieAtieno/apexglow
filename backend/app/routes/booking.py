from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..extensions import db
from ..models.booking import Booking, BookingStatus  # Imported BookingStatus enum class
from ..models.user import User

bookings_bp = Blueprint("bookings", __name__)


# ============================================================
# CREATE BOOKING: Check a vehicle with its plate into the bay
# ============================================================
@bookings_bp.route("/bookings", methods=["POST"])
@jwt_required()
def create_booking():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    
    customer_name = data.get("customer_name", "").strip()
    customer_phone = data.get("customer_phone", "").strip()
    vehicle_plate = data.get("vehicle_plate", "").strip().upper()
    carwash_id = data.get("carwash_id")
    service_id = data.get("service_id")
    assigned_staff_id = data.get("assigned_staff_id")
    
    # Validation Checks
    if not all([customer_name, customer_phone, vehicle_plate, carwash_id, service_id]):
        return jsonify({
            "error": "Customer name, phone, vehicle_plate, carwash_id, and service_id are required"
        }), 400
        
    # Security Check: Verify user exists and has tenant access to this specific car wash bay
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"error": "User profile not found"}), 404

    if not user.can_access_carwash(carwash_id):
        return jsonify({"error": "Unauthorized access to this car wash queue"}), 403

    try:
        #Initialize and save ticket into the queue using the native Enum instance
        new_booking = Booking(
            customer_name=customer_name,
            customer_phone=customer_phone,
            vehicle_plate=vehicle_plate,
            carwash_id=carwash_id,
            service_id=service_id,
            assigned_staff_id=assigned_staff_id if assigned_staff_id else None,
            status=BookingStatus.PENDING
        )
        
        db.session.add(new_booking)
        db.session.commit()
        
        return jsonify({
            "message": "Vehicle checked into the wash queue successfully!",
            "booking": {
                "id": new_booking.id,
                "customer_name": new_booking.customer_name,
                "vehicle_plate": new_booking.vehicle_plate,
                "status": new_booking.status.value,  # Returns  string value for JSON serialization
                "booking_time": new_booking.booking_time.isoformat() if new_booking.booking_time else None
            }
        }), 201
        
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Failed to check in vehicle"}), 500


# ============================================================
#LIVE QUEUE: Display vehicle plate streams on dashboard screen
# ============================================================
@bookings_bp.route("/bookings/queue/<string:carwash_id>", methods=["GET"])
@jwt_required()
def get_live_queue(carwash_id):
    user_id = get_jwt_identity()
    user = db.session.get(User, user_id)
    
    if not user or not user.can_access_carwash(carwash_id):
        return jsonify({"error": "Unauthorized access to this car wash workspace."}), 403
        
    try:
        
        query = (
            db.select(Booking)
            .where(
                Booking.carwash_id == carwash_id,
                Booking.status.in_([BookingStatus.PENDING, BookingStatus.IN_PROGRESS])
            )
            .order_by(Booking.booking_time.asc())
        )
        active_queue = db.session.execute(query).scalars().all()
        
        queue_data = [{
            "booking_id": ticket.id,
            "customer_name": ticket.customer_name,
            "customer_phone": ticket.customer_phone,
            "vehicle_plate": ticket.vehicle_plate,
            "status": ticket.status.value,  # Extracts raw clean string for UI presentation layers
            "service_name": ticket.service.name if ticket.service else "Unknown Service",
            "price": ticket.service.price if ticket.service else 0.0,
            "assigned_staff": ticket.assigned_staff.position if ticket.assigned_staff else "Unassigned",
            "checked_in_at": ticket.booking_time.strftime("%Y-%m-%d %H:%M:%S") if ticket.booking_time else None
        } for ticket in active_queue]
        
        return jsonify({
            "carwash_id": carwash_id,
            "total_vehicles_waiting": len(queue_data),
            "live_queue": queue_data
        }), 200
        
    except Exception:
        return jsonify({"error": "Failed to load live queue"}), 500


# ============================================================
# UPDATE BOOKING STATUS: Advance wash status states smoothly
# ============================================================
@bookings_bp.route("/bookings/<string:booking_id>/status", methods=["PUT"])
@jwt_required()
def update_booking_status(booking_id):
    user_id = get_jwt_identity()
    user = db.session.get(User, user_id)
    data = request.get_json() or {}
    
    new_status_str = data.get("status", "").strip()
    
    # Structural conversion safety check: Tries to find target within BookingStatus options
    try:
        target_status = BookingStatus(new_status_str)
    except ValueError:
        return jsonify({
            "error": f"Invalid status. Must be one of: {[s.value for s in BookingStatus]}"
        }), 400
        
    if not user:
        return jsonify({"error": "User profile not found"}), 404

    # Fetch booking target cleanly
    ticket = db.session.get(Booking, booking_id)
    if not ticket:
        return jsonify({"error": "Booking record not found"}), 404
        
    # Cross-tenant mapping validation
    if not user.can_access_carwash(ticket.carwash_id):
        return jsonify({"error": "Booking workspace validation failed."}), 403
        
    try:
        # Assign the validated safe Enum structure directly
        ticket.status = target_status
        db.session.commit()
        
        return jsonify({
            "message": f"Vehicle status updated to '{ticket.status.value}' successfully!",
            "booking": {
                "id": ticket.id,
                "customer_name": ticket.customer_name,
                "vehicle_plate": ticket.vehicle_plate,
                "status": ticket.status.value
            }
        }), 200
        
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Failed to update booking status"}), 500
