from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from ..extensions import db
from ..models.user import User

def roles_required(*allowed_roles):
    """
    Custom decorator to restrict route access to specific user roles.
    Example use: @roles_required("owner", "manager")
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()
            user = db.session.get(User, user_id)
            
            # 1. Ensure user account still exists
            if not user:
                return jsonify({"error": "User profile not found"}), 404
                
            # 2. Block inactive or suspended users instantly
            if not user.is_active:
                return jsonify({"error": "Account is deactivated"}), 403
                
            # 3. Restrict actions based on the allowed role strings
            if user.role not in allowed_roles:
                return jsonify({
                    "error": f"Unauthorized. This action requires one of the following roles: {', '.join(allowed_roles)}"
                }), 403
                
            return fn(*args, **kwargs)
        return wrapper
    return decorator
