from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.admin import Admin
from app import db

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admins', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    return jsonify([admin.to_dict() for admin in admins]), 200

@admin_bp.route('/admins/<int:admin_id>', methods=['GET'])
def get_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    return jsonify(admin.to_dict()), 200

@admin_bp.route('/admins', methods=['POST'])
def create_admin():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password are required'}), 400
    
    existing_admin = Admin.query.filter_by(username=data['username']).first()
    if existing_admin:
        return jsonify({'message': 'Username already exists'}), 409
    
    hashed_password = generate_password_hash(data['password'])
    new_admin = Admin(
        username=data['username'],
        password=hashed_password
    )
    db.session.add(new_admin)
    db.session.commit()
    return jsonify(new_admin.to_dict()), 201

@admin_bp.route('/admins/<int:admin_id>', methods=['PUT'])
def update_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    data = request.get_json()
    
    if 'username' in data:
        admin.username = data['username']
    if 'password' in data:
        admin.password = generate_password_hash(data['password'])
    
    db.session.commit()
    return jsonify(admin.to_dict()), 200

@admin_bp.route('/admins/<int:admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    db.session.delete(admin)
    db.session.commit()
    return '', 204
