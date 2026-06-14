from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models.booking import Booking
from ..models.user import User

bookings_bp = Blueprint("bookings", __name__)

# ------------------------------------------------------------
# 1. CREATE BOOKING: Check a vehicle with its plate into the bay
# ------------------------------------------------------------
@bookings_bp.route("/bookings", methods=["POST"])
@jwt_required()
def create_booking():
    data = request.get_json() or {}
    
    customer_name = data.get("customer_name")
    customer_phone = data.get("customer_phone")
    vehicle_plate = data.get("vehicle_plate") # <--- Capturing plate parameter
    carwash_id = data.get("carwash_id")
    service_id = data.get("service_id")
    assigned_staff_id = data.get("assigned_staff_id")
    
    if not all([customer_name, customer_phone, vehicle_plate, carwash_id, service_id]):
        return jsonify({"error": "Customer name, phone, vehicle_plate, carwash_id, and service_id are required"}), 400
        
    try:
        new_booking = Booking(
            customer_name=customer_name,
            customer_phone=customer_phone,
            vehicle_plate=vehicle_plate.upper().strip(), # Clean and make it uniform uppercase
            carwash_id=carwash_id,
            service_id=service_id,
            assigned_staff_id=assigned_staff_id if assigned_staff_id else None,
            status="Pending"
        )
        
        db.session.add(new_booking)
        db.session.commit()
        
        return jsonify({
            "message": "Vehicle checked into the wash queue successfully!",
            "booking": {
                "id": new_booking.id,
                "customer_name": new_booking.customer_name,
                "vehicle_plate": new_booking.vehicle_plate,
                "status": new_booking.status,
                "booking_time": new_booking.booking_time
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to check in vehicle", "details": str(e)}), 500


# ------------------------------------------------------------
# 2. GET LIVE QUEUE: Display vehicle plate streams on screen
# ------------------------------------------------------------
@bookings_bp.route("/bookings/queue/<string:carwash_id>", methods=["GET"])
@jwt_required()
def get_live_queue(carwash_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user or carwash_id not in user.accessible_carwash_ids:
        return jsonify({"error": "Unauthorized access to this car wash workspace."}), 403
        
    try:
        active_queue = Booking.query.filter(
            Booking.carwash_id == carwash_id,
            Booking.status.in_(["Pending", "In Progress"])
        ).order_by(Booking.booking_time.asc()).all()
        
        queue_data = [{
            "booking_id": ticket.id,
            "customer_name": ticket.customer_name,
            "customer_phone": ticket.customer_phone,
            "vehicle_plate": ticket.vehicle_plate, # <--- Exposing plate for dashboard display
            "status": ticket.status,
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
    except Exception as e:
        return jsonify({"error": "Failed to load live queue", "details": str(e)}), 500


# ------------------------------------------------------------
# 3. UPDATE BOOKING STATUS: Advance status smoothly
# ------------------------------------------------------------
@bookings_bp.route("/bookings/<string:booking_id>/status", methods=["PUT"])
@jwt_required()
def update_booking_status(booking_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    data = request.get_json() or {}
    
    new_status = data.get("status")
    allowed_statuses = ["Pending", "In Progress", "Completed", "Cancelled"]
    if new_status not in allowed_statuses:
        return jsonify({"error": f"Invalid status. Must be one of: {', '.join(allowed_statuses)}"}), 400
        
    ticket = Booking.query.get(booking_id)
    if not ticket or ticket.carwash_id not in user.accessible_carwash_ids:
        return jsonify({"error": "Booking workspace validation failed."}), 403
        
    try:
        ticket.status = new_status
        db.session.commit()
        
        return jsonify({
            "message": f"Vehicle status updated to '{ticket.status}' successfully!",
            "booking": {
                "id": ticket.id,
                "customer_name": ticket.customer_name,
                "vehicle_plate": ticket.vehicle_plate, # <--- Render it safely here
                "status": ticket.status
            }
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update booking status", "details": str(e)}), 500
