from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import Config

from app.routes import user_bp, seller_bp, admin_bp, product_bp

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    
    db.init_app(app)
    
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(seller_bp, url_prefix='/api/sellers')
    app.register_blueprint(admin_bp, url_prefix='/api/admins')
    app.register_blueprint(product_bp, url_prefix='/api/products')

    return app
