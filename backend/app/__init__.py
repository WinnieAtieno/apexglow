from flask import Flask
from .config import Config
from .extensions import db, jwt, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 1. Initialize core system extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # 2. Load your multi-tenant models explicitly
    from .models.user import User
    from .models.carwash import CarWash
    from .models.staff import Staff
    from .models.service import Service
    from .models.booking import Booking
    
    # 3. Import your operational routing blueprints
    from .routes.main import main_bp
    from .routes.auth import auth_bp
    from .routes.business import business_bp  
    from .routes.services import services_bp  
    from .routes.staff import staff_bp      
    from .routes.booking import bookings_bp  

    # 4. Register blueprints into the main Flask application
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    
    # Registering your multi-tenant SaaS API routers with clean prefixes
    app.register_blueprint(business_bp, url_prefix="/api") 
    app.register_blueprint(services_bp, url_prefix="/api") 
    app.register_blueprint(staff_bp, url_prefix="/api")    # <--- Registered Staff
    app.register_blueprint(bookings_bp, url_prefix="/api") # <--- Registered Bookings

    return app
