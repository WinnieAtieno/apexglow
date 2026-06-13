from flask import Blueprint, jsonify,request
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import db
from ..models.user import User



auth_bp = Blueprint("auth",__name__)



@auth_bp.route('/register', methods=["POST"])
def register():
    data = request.get_json()
 
    fullname = data.get("fullname")
    email = data.get("email")
    password = data.get("password")

       # check if user exists in DB
    user_exists = User.query.filter_by(email=email).first()
    
    if user_exists:
        return jsonify({"error": "User already exists"}), 400
    
    hashed_password = generate_password_hash(password)

    newUser = User(
        fullname=fullname,
        email = email,
        password =hashed_password
    )

    db.session.add(newUser)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}),200

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email= data.get("email")
    password = data.get("password")
    
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    if not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user.id,
            "fullname": user.fullname,
            "email": user.email,
            "role": user.role
        }
    })