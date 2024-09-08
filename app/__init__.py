from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Initialize CORS
    cors_origins = app.config.get('CORS_ORIGINS', '*')
    CORS(app, resources={r"/*": {"origins": cors_origins}})
    
    # Import models to ensure they are registered with SQLAlchemy
    from app.models import User, Product, Seller, Admin, UnapprovedProduct, ArchivedProduct, Order, OrderItem, AdminActivity, AdminNotification, SellerActivity, SellerNotification, DeletedProduct
    
    # Register blueprints
    from app.routes.user_routes import user_bp
    from app.routes.seller_routes import seller_bp
    from app.routes.admin_routes import admin_bp
    from app.routes.product_routes import product_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(seller_bp, url_prefix='/api/sellers')
    app.register_blueprint(admin_bp, url_prefix='/api/admins')
    app.register_blueprint(product_bp, url_prefix='/api/products')

    return app
