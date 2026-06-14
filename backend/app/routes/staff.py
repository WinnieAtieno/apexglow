from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..extensions import db
from ..models.staff import Staff
from ..models.user import User
from werkzeug.security import generate_password_hash

staff_bp = Blueprint("staff", __name__)

# ------------------------------------------------------------
# STAFF ONBOARDING: Link a login User to a working Location
# ------------------------------------------------------------
@staff_bp.route("/staff", methods=["POST"])
@jwt_required() # Securely blocks unauthorized traffic
def create_staff():
    data = request.get_json() or {}
    
    email = data.get("email")
    password = data.get("password")
    name = data.get("name")
    position = data.get("position", "washer") # washer, cashier, manager
    carwash_id = data.get("carwash_id")
    
    if not all([email, password, name, carwash_id]):
        return jsonify({"error": "Email, password, name, and carwash_id are required"}), 400
        
    try:
        # 1. FIXED: Removed name=name here because your User model doesn't have that column
        new_user = User(
            email=email,
            password_hash=generate_password_hash(password),
            role="staff" # Mark system access level explicitly as staff
        )
        db.session.add(new_user)
        db.session.flush() # Immediately fetch the new staff member's User UUID string
        
        # 2. Bind that authentication User to their workplace location entry
        # We append the name straight to the position so it saves beautifully!
        new_staff = Staff(
            position=f"{name} ({position})",
            user_id=new_user.id,
            carwash_id=carwash_id
        )
        db.session.add(new_staff)
        db.session.commit()
        
        return jsonify({
            "message": "Staff member onboarded successfully!",
            "staff": {
                "id": new_staff.id,
                "position": new_staff.position,
                "carwash_id": new_staff.carwash_id
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to onboard staff member", "details": str(e)}), 500
