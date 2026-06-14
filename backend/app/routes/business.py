from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models.carwash import CarWash

business_bp = Blueprint("business", __name__)



# ------------------------------------------------------------
# PHASE 2: Onboarding Setup Wizard (Workspace Creation)
# ------------------------------------------------------------
@business_bp.route("/business/setup", methods=["POST"])
@jwt_required() # Securely blocks unauthenticated traffic
def setup_business():
    # Automatically extracts the logged-in User's UUID string from the token
    user_id = get_jwt_identity() 
    data = request.get_json() or {}
    
    name = data.get("name")
    subdomain = data.get("subdomain")
    location = data.get("location")
    
    # 1. Enforce validation on business-critical fields
    if not name or not subdomain:
        return jsonify({"error": "Business name and web address subdomain are required"}), 400
        
    # 2. Sanitize user input (lowercase and remove trailing spaces for the URL routing)
    clean_subdomain = subdomain.lower().strip()
        
    # 3. Safety Check: Verify that the target subdomain isn't already taken
    subdomain_exists = CarWash.query.filter_by(subdomain=clean_subdomain).first()
    if subdomain_exists:
        return jsonify({"error": "This subdomain is already claimed by another business"}), 400
        
    try:
        # 4. Initialize and map the Car Wash database row
        new_wash = CarWash(
            name=name,
            subdomain=clean_subdomain,
            location=location, # Will save text string, or default to null if empty
            owner_id=user_id   # Securely locks the shop workspace to the logged-in User UUID
        )
        
        db.session.add(new_wash)
        db.session.commit()
        
        return jsonify({
            "message": "Your ApexGlow business workspace is fully ready!",
            "business": {
                "id": new_wash.id,
                "name": new_wash.name,
                "subdomain": new_wash.subdomain,
                "location": new_wash.location
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to set up workspace", "details": str(e)}), 500

# ------------------------------------------------------------
# UPDATE BUSINESS SETTINGS (e.g., Setting the missing Location)
# ------------------------------------------------------------
@business_bp.route("/business/<string:carwash_id>", methods=["PUT"])
@jwt_required()
def update_business(carwash_id):
    user_id = get_jwt_identity() # Extracts the logged-in user's UUID string
    data = request.get_json() or {}
    
    # Find the specific car wash location
    wash = CarWash.query.get(carwash_id)
    
    if not wash:
        return jsonify({"error": "Car wash business workspace not found"}), 404
        
    # SECURITY CHECK: Ensure the logged-in user actually owns this business!
    if wash.owner_id != user_id:
        return jsonify({"error": "Unauthorized. You do not own this business workspace."}), 403
        
    try:
        # Dynamically update the fields if they are sent in Postman
        if "name" in data:
            wash.name = data["name"]
        if "location" in data:
            wash.location = data["location"] # <--- This is how they update their address!
            
        db.session.commit()
        
        return jsonify({
            "message": "Business profile updated successfully!",
            "business": {
                "id": wash.id,
                "name": wash.name,
                "subdomain": wash.subdomain,
                "location": wash.location # Will now show your updated address!
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update business profile", "details": str(e)}), 500
