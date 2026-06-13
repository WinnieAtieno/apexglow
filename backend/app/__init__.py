from flask import Flask
from .config import Config
from .extensions import db, jwt, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # init extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # IMPORTANT: load models package
    from .models import User

    # register blueprints
    from .routes.main import main_bp
    from .routes.auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app