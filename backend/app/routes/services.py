from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..extensions import db
from ..models.service import Service

services_bp = Blueprint("services", __name__)

# ------------------------------------------------------------
# PHASE 3: Create Menu Item (SaaS Isolated Setup)
# ------------------------------------------------------------
@services_bp.route("/services", methods=["POST"])
@jwt_required() # Protects route so only logged-in managers/owners can edit menus
def create_service():
    data = request.get_json() or {}
    
    name = data.get("name")
    price = data.get("price")
    carwash_id = data.get("carwash_id") # Passed from the active workspace dashboard
    
    # Enforce input validations
    if not all([name, price, carwash_id]):
        return jsonify({"error": "Service name, price, and carwash_id are required"}), 400
        
    try:
        # Initialize and link the new wash package to the target location UUID string
        new_service = Service(
            name=name,
            price=float(price),
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
        
    except ValueError:
        return jsonify({"error": "Price must be a valid decimal or integer number"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to add service package", "details": str(e)}), 500
