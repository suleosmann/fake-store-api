from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate

    # Import and register blueprints
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    # Import models to ensure they are registered with SQLAlchemy
    from . import models

    return app
