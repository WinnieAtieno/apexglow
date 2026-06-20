from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..extensions import db
from ..models.user import User
from ..models.staff import Staff
from ..utils.decorators import roles_required  # Imported for backend security

staff_bp = Blueprint("staff", __name__)


# ============================================================
# CREATE: Onboard Staff Member & Create Auth Account Shell
# ============================================================
@staff_bp.route("/staff", methods=["POST"])
@jwt_required()
@roles_required("owner", "manager")  # Blocks unauthorized staff from hiring people
def create_staff():
    current_user_id = get_jwt_identity()
    data = request.get_json() or {}
    
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")
    name = data.get("name", "").strip()
    position = data.get("position", "washer").strip().lower()  # washer, cashier, manager
    carwash_id = data.get("carwash_id")
    
    # Enforce Mandatory Field Validations
    if not all([email, password, name, carwash_id]):
        return jsonify({"error": "Email, password, name, and carwash_id are required"}), 400

    if len(password) < 8:
        return jsonify({"error": "Password must contain at least 8 characters"}), 400
        
    # Multi-Tenant Check: Ensure this logged-in manager/owner actually has rights over this specific shop
    current_user = db.session.get(User, current_user_id)
    if not current_user or not current_user.can_access_carwash(carwash_id):
        return jsonify({"error": "Unauthorized access to this workspace roster"}), 403

    # Double-check System Duplications
    existing_user = db.session.execute(
        db.select(User).filter_by(email=email)
    ).scalar_one_or_none()
    
    if existing_user:
        return jsonify({"error": "Email is already registered in the system"}), 400

    try:
        # Initialize User Core Account Profile (matches your model exactly)
        new_user = User(
            full_name=name,
            email=email,
            role="staff" 
        )
        new_user.password = password  
        
        db.session.add(new_user)
        db.session.flush() 

        # Build Staff Workspace Link Entity
        new_staff = Staff(
            position=position,
            user_id=new_user.id,
            carwash_id=carwash_id
        )
        db.session.add(new_staff)
        db.session.commit()
        
        return jsonify({
            "message": "Staff member onboarded successfully!",
            "staff": {
                "id": new_staff.id,
                "user_id": new_staff.user_id,
                "full_name": new_user.full_name,
                "email": new_user.email,
                "position": new_staff.position,
                "carwash_id": new_staff.carwash_id
            }
        }), 201
        
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Failed to safely onboard staff profile"}), 500


# ============================================================
# View Employee Roster of a Specific Location
# ============================================================
@staff_bp.route("/staff/carwash/<string:carwash_id>", methods=["GET"])
@jwt_required()
def get_shop_roster(carwash_id):
    current_user_id = get_jwt_identity()
    current_user = db.session.get(User, current_user_id)

    # Cross-tenant mapping validation
    if not current_user or not current_user.can_access_carwash(carwash_id):
        return jsonify({"error": "Unauthorized access to this workspace roster"}), 403

    # Query joining User to grab name and email fields
    query = db.select(Staff).join(User).where(Staff.carwash_id == carwash_id)
    roster = db.session.execute(query).scalars().all()

    return jsonify({
        "staff": [
            {
                "id": emp.id,
                "user_id": emp.user_id,
                "full_name": emp.user.full_name,
                "email": emp.user.email,
                "position": emp.position,
                "is_active": emp.user.is_active
            } for emp in roster
        ]
    }), 200


# ============================================================
# UPDATE: Modify Employee Role Position or Account Status
# ============================================================
@staff_bp.route("/staff/<string:staff_id>", methods=["PUT"])
@jwt_required()
@roles_required("owner", "manager")  # Blocks unauthorized staff from editing coworkers
def update_staff(staff_id):
    current_user_id = get_jwt_identity()
    data = request.get_json() or {}
    
    emp = db.session.get(Staff, staff_id)
    if not emp:
        return jsonify({"error": "Staff profile record not found"}), 404

    current_user = db.session.get(User, current_user_id)
    if not current_user or not current_user.can_access_carwash(emp.carwash_id):
        return jsonify({"error": "Unauthorized access to this workspace roster"}), 403

    try:
        if "position" in data and data["position"].strip():
            emp.position = data["position"].strip().lower()

        # Handle account suspensions cleanly through the linked user profile
        if "is_active" in data:
            emp.user.is_active = bool(data["is_active"])

        db.session.commit()
        return jsonify({"message": "Staff assignment information modified successfully"}), 200
        
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Failed to alter employee tracking data"}), 500


# ============================================================
# DELETE: Remove Staff Access Assignment Entirely
# ============================================================
@staff_bp.route("/staff/<string:staff_id>", methods=["DELETE"])
@jwt_required()
@roles_required("owner", "manager")  # Blocks regular staff from firing people
def terminate_staff(staff_id):
    current_user_id = get_jwt_identity()

    emp = db.session.get(Staff, staff_id)
    if not emp:
        return jsonify({"error": "Staff profile record not found"}), 404

    current_user = db.session.get(User, current_user_id)
    if not current_user or not current_user.can_access_carwash(emp.carwash_id):
        return jsonify({"error": "Unauthorized access to this workspace roster"}), 403

    try:
        linked_user = emp.user
        
        db.session.delete(emp)
        db.session.delete(linked_user)  
        db.session.commit()
        
        return jsonify({"message": "Staff member offboarded and credential accounts purged"}), 200
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Failed to remove staff member"}), 500
