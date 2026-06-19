from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)

from ..extensions import db
from ..models.user import User

auth_bp = Blueprint("auth", __name__)


# ============================================================
# REGISTER
# ============================================================
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}

    full_name = data.get("full_name", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not full_name or not email or not password:
        return jsonify({"error": "Full name, email, and password are required"}), 400

    if len(full_name) < 2:
        return jsonify({"error": "Full name must be at least 2 characters"}), 400

    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email is already registered"}), 400

    try:
        user = User(
            full_name=full_name,
            email=email,
            role="owner"
        )

        user.password = password  

        db.session.add(user)
        db.session.commit()

        return jsonify({
            "message": "Account created successfully",
            "access_token": create_access_token(identity=user.id),
            "refresh_token": create_refresh_token(identity=user.id),
            "user": {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "role": user.role,
                "has_business": False
            }
        }), 201

    except Exception:
        db.session.rollback()
        return jsonify({"error": "Registration failed"}), 500


# ============================================================
# LOGIN
# ============================================================
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}

    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    # Generic error (prevents user enumeration)
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    if not user.is_active:
        return jsonify({"error": "Account is deactivated"}), 403

    return jsonify({
        "access_token": create_access_token(identity=user.id),
        "refresh_token": create_refresh_token(identity=user.id),
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role,
            "accessible_shops": user.accessible_carwash_ids
        }
    }), 200


# ============================================================
# REFRESH TOKEN
# ============================================================
@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()

    return jsonify({
        "access_token": create_access_token(identity=user_id)
    }), 200


# ============================================================
# CURRENT USER
# ============================================================
@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()

    user = db.session.get(User, user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not user.is_active:
        return jsonify({"error": "Account is deactivated"}), 403

    return jsonify({
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role,
            "has_business": len(user.carwashes) > 0,
            "accessible_shops": user.accessible_carwash_ids
        }
    }), 200


# ============================================================
# TEST ENDPOINT
# ============================================================
@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify({
        "message": "JWT is working",
        "user_id": get_jwt_identity()
    }), 200