from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..extensions import db
from ..models.user import User
from ..models.carwash import CarWash
from ..utils.decorators import roles_required 

business_bp = Blueprint("business", __name__)


# ============================================================
# CREATE: Setup Business Workspace
# ============================================================
@business_bp.route("/business/setup", methods=["POST"])
@jwt_required()
@roles_required("owner")  # Staff members are blocked from initiating setup
def setup_business():
    user_id = get_jwt_identity()
    data = request.get_json() or {}

    name = data.get("name", "").strip()
    subdomain = data.get("subdomain", "").strip().lower()
    location = data.get("location", "").strip()

    #  Enforce Validation
    if not name or not subdomain:
        return jsonify({"error": "Business name and subdomain are required"}), 400

    # Authorization Check: Ensure the user is an owner
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"error": "User profile not found"}), 404
        
    if user.role != "owner":
        return jsonify({"error": "Only workspace owners can register business profiles"}), 403

    # Duplicate Domain Lookup 
    subdomain_exists = db.session.execute(
        db.select(CarWash).filter_by(subdomain=subdomain)
    ).scalar_one_or_none()

    if subdomain_exists:
        return jsonify({"error": "Subdomain is already taken"}), 400

    try:
        # 4. Create Workspace Shell
        new_wash = CarWash(
            name=name,
            subdomain=subdomain,
            location=location if location else None,
            owner_id=user.id
        )

        db.session.add(new_wash)
        db.session.commit()

        return jsonify({
            "message": "Workspace created successfully",
            "business": new_wash.to_dict()
        }), 201

    except Exception:
        db.session.rollback()
        return jsonify({"error": "Workspace setup configuration failed"}), 500


# ============================================================
# List All Accessible Car Washes for the Current User
# ============================================================
@business_bp.route("/business/my-shops", methods=["GET"])
@jwt_required()
def get_my_shops():
    user_id = get_jwt_identity()
    user = db.session.get(User, user_id)

    if not user:
        return jsonify({"error": "User profile not found"}), 404

    # Fetch accessible locations based on role logic (Owners get all their shops, staff get assigned shop)
    accessible_ids = user.accessible_carwash_ids
    
    if not accessible_ids:
        return jsonify({"businesses": []}), 200

    query = db.select(CarWash).where(CarWash.id.in_(accessible_ids))
    shops = db.session.execute(query).scalars().all()

    return jsonify({
        "businesses": [shop.to_dict() for shop in shops]
    }), 200


# ============================================================
#  Fetch Details of a Single Specific Business Profile
# ============================================================
@business_bp.route("/business/<string:carwash_id>", methods=["GET"])
@jwt_required()
def get_business(carwash_id):
    user_id = get_jwt_identity()
    
    wash = db.session.get(CarWash, carwash_id)
    if not wash:
        return jsonify({"error": "Business profile not found"}), 404

    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"error": "User profile not found"}), 404

    # Permission check via User Model property (Allows allowed staff/owners of this specific shop)
    if not user.can_access_carwash(carwash_id):
        return jsonify({"error": "Unauthorized access to this business profile"}), 403

    return jsonify({
        "business": wash.to_dict()
    }), 200


# ============================================================
# UPDATE: Modify Existing Profile Metadata
# ============================================================
@business_bp.route("/business/<string:carwash_id>", methods=["PUT"])
@jwt_required()
@roles_required("owner")  # Restricts editing business configurations to owners only
def update_business(carwash_id):
    user_id = get_jwt_identity()
    data = request.get_json() or {}

    wash = db.session.get(CarWash, carwash_id)
    if not wash:
        return jsonify({"error": "Business profile not found"}), 404

    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"error": "User profile not found"}), 404

    # Immutable Field Prevention
    if "subdomain" in data:
        return jsonify({"error": "Subdomain cannot be changed after setup"}), 400

    # Access Permission Check
    if not user.can_access_carwash(carwash_id):
        return jsonify({"error": "Unauthorized access to this business profile"}), 403

    try:
        if "name" in data and data["name"].strip():
            wash.name = data["name"].strip()

        if "location" in data and data["location"].strip():
            wash.location = data["location"].strip()

        db.session.commit()

        return jsonify({
            "message": "Business updated successfully",
            "business": wash.to_dict()
        }), 200

    except Exception:
        db.session.rollback()
        return jsonify({"error": "Failed to update business profile metadata"}), 500


# ============================================================
# DELETE: Permanently Delete a Business Workspace
# ============================================================
@business_bp.route("/business/<string:carwash_id>", methods=["DELETE"])
@jwt_required()
@roles_required("owner")  # Prevent staff members from executing absolute terminations
def delete_business(carwash_id):
    user_id = get_jwt_identity()

    wash = db.session.get(CarWash, carwash_id)
    if not wash:
        return jsonify({"error": "Business profile not found"}), 404

   
    if wash.owner_id != user_id:
        return jsonify({"error": "Only the primary business owner can close down this workspace"}), 403

    try:
        db.session.delete(wash)
        db.session.commit()

        return jsonify({
            "message": f"Business '{wash.name}' has been permanently closed and removed."
        }), 200

    except Exception:
        db.session.rollback()
        return jsonify({"error": "Failed to safely dissolve this business profile"}), 500
