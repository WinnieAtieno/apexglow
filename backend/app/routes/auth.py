from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)

from ..extensions import db
from ..models.user import User

auth_bp = Blueprint("auth", __name__)


# ------------------------------------------------------------
# PHASE 1: Frictionless Registration (Email & Password Only)
# ------------------------------------------------------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}

    email = data.get("email")
    password = data.get("password")

    # 1. Enforce only the absolute bare minimum details
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # 2. Safety Check: Avoid duplicate registrations
    user_exists = User.query.filter_by(email=email).first()
    if user_exists:
        return jsonify({"error": "User email already registered"}), 400

    try:
        hashed_password = generate_password_hash(password)

        # 3. Create the empty user account shell (defaults to role='owner')
        new_user = User(
            email=email,
            password_hash=hashed_password,
            role="owner"
        )
        
        db.session.add(new_user)
        db.session.commit() # Saves cleanly to the users table immediately

        # 4. Generate immediate access tokens so they are auto-logged in
        access_token = create_access_token(identity=str(new_user.id))
        refresh_token = create_refresh_token(identity=str(new_user.id))

        return jsonify({
            "message": "Account created successfully!",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": {
                "id": new_user.id,
                "email": new_user.email,
                "role": new_user.role,
                "has_business": False # Flags the frontend to load the onboarding wizard page
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Registration failed.", "details": str(e)}), 500


# -------------------------
# LOGIN
# -------------------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": {
            "id": user.id,
            "email": user.email,
            "role": user.role,
            "accessible_shops": user.accessible_carwash_ids 
        }
    }), 200
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

# ------------------------------------------------------------
# TOKEN REFRESH: Exchange a Refresh Token for a new Access Token
# ------------------------------------------------------------
@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True) # CRITICAL: This strictly requires a REFRESH token, not an access token!
def refresh():
    # 1. Automatically extracts the User's UUID string from the active refresh token context
    current_user_id = get_jwt_identity()
    
    # 2. Cook up a fresh, unexpired access token for their session
    new_access_token = create_access_token(identity=str(current_user_id))
    
    return jsonify({
        "access_token": new_access_token,
        "message": "Access token refreshed successfully"
    }), 200


# -------------------------
# PROTECTED ROUTE
# -------------------------
@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    user_id = get_jwt_identity()

    return jsonify({
        "message": "JWT is working",
        "user_id": user_id
    }), 200


# -------------------------
# DASHBOARD
# -------------------------
@auth_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "User context invalid"}), 404

    # Extract all car wash storefront details owned by this user
    shops_data = []
    if user.role == "owner":
        shops_data = [{
            "id": shop.id,
            "name": shop.name,
            "subdomain": shop.subdomain,
            "location": shop.location
        } for shop in user.carwashes]

    return jsonify({
        "message": "Welcome to ApexGlow Dashboard",
        "user": {
            "id": user.id,
            "email": user.email,
            "role": user.role
        },
        "businesses": shops_data
    }), 200
