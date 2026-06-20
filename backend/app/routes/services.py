from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..extensions import db
from ..models.user import User
from ..models.service import Service
from ..utils.decorators import roles_required  # Imported for backend security

services_bp = Blueprint("services", __name__)


# ============================================================
# CREATE: Add New Wash Package to a Menu
# ============================================================
@services_bp.route("/services", methods=["POST"])
@jwt_required()
@roles_required("owner", "manager")  # Blocks regular staff from adding menu items
def create_service():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    
    name = data.get("name", "").strip()
    price = data.get("price")
    carwash_id = data.get("carwash_id")
    
    # Enforce Input Validation
    if not name or price is None or not carwash_id:
        return jsonify({"error": "Service name, price, and carwash_id are required"}), 400
        
    # Security Check: Verify user exists and can modify this specific car wash menu
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"error": "User profile not found"}), 404

    if not user.can_access_carwash(carwash_id):
        return jsonify({"error": "Unauthorized access to this car wash menu"}), 403

    try:
        #  Handle decimal conversion safely
        numeric_price = float(price)
        if numeric_price < 0:
            return jsonify({"error": "Price cannot be a negative value"}), 400

        # Save to Database
        new_service = Service(
            name=name,
            price=numeric_price,
            carwash_id=carwash_id
        )
        
        db.session.add(new_service)
        db.session.commit()
        
        return jsonify({
            "message": "Wash package added to your menu successfully!",
            "service": {
                "id": new_service.id,
                "name": new_service.name,
                "price": new_service.price,
                "carwash_id": new_service.carwash_id
            }
        }), 201
        
    except (ValueError, TypeError):
        return jsonify({"error": "Price must be a valid decimal or integer number"}), 400
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Failed to add service package"}), 500


# ============================================================
#List All Services for a Specific Car Wash
# ============================================================
@services_bp.route("/services/carwash/<string:carwash_id>", methods=["GET"])
@jwt_required()
def get_carwash_services(carwash_id):
    user_id = get_jwt_identity()
    user = db.session.get(User, user_id)

    # Allow all active staff/owners inside this shop to view the pricing menu
    if not user or not user.can_access_carwash(carwash_id):
        return jsonify({"error": "Unauthorized access to this car wash menu"}), 403

   
    query = db.select(Service).where(Service.carwash_id == carwash_id).order_by(Service.name)
    services = db.session.execute(query).scalars().all()

    return jsonify({
        "services": [
            {
                "id": s.id,
                "name": s.name,
                "price": s.price,
                "carwash_id": s.carwash_id
            } for s in services
        ]
    }), 200


# ============================================================
# UPDATE: Modify Price or Name of an Existing Menu Item
# ============================================================
@services_bp.route("/services/<string:service_id>", methods=["PUT"])
@jwt_required()
@roles_required("owner", "manager")  # Blocks regular staff from editing prices
def update_service(service_id):
    user_id = get_jwt_identity()
    data = request.get_json() or {}

    service = db.session.get(Service, service_id)
    if not service:
        return jsonify({"error": "Service package not found"}), 404

    user = db.session.get(User, user_id)
    if not user or not user.can_access_carwash(service.carwash_id):
        return jsonify({"error": "Unauthorized access to this car wash menu"}), 403

    try:
        if "name" in data and data["name"].strip():
            service.name = data["name"].strip()

        if "price" in data:
            numeric_price = float(data["price"])
            if numeric_price < 0:
                return jsonify({"error": "Price cannot be a negative value"}), 400
            service.price = numeric_price

        db.session.commit()

        return jsonify({
            "message": "Service package updated successfully",
            "service": {
                "id": service.id,
                "name": service.name,
                "price": service.price,
                "carwash_id": service.carwash_id
            }
        }), 200

    except (ValueError, TypeError):
        return jsonify({"error": "Price must be a valid decimal or integer number"}), 400
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Failed to update service package"}), 500


# ============================================================
# DELETE: Remove a Service Package from a Menu Completely
# ============================================================
@services_bp.route("/services/<string:service_id>", methods=["DELETE"])
@jwt_required()
@roles_required("owner", "manager")  # Blocks regular staff from deleting menu items
def delete_service(service_id):
    user_id = get_jwt_identity()

    service = db.session.get(Service, service_id)
    if not service:
        return jsonify({"error": "Service package not found"}), 404

    user = db.session.get(User, user_id)
    if not user or not user.can_access_carwash(service.carwash_id):
        return jsonify({"error": "Unauthorized access to this car wash menu"}), 403

    try:
        db.session.delete(service)
        db.session.commit()
        return jsonify({"message": f"Service '{service.name}' has been successfully removed"}), 200
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Failed to remove service package"}), 500
