from flask import Blueprint, request, jsonify
from app.models.admin import Admin
from app import db

bp = Blueprint('admin_routes', __name__)

@bp.route('/admins', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    return jsonify([admin.to_dict() for admin in admins])

@bp.route('/admins/<int:admin_id>', methods=['GET'])
def get_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    return jsonify(admin.to_dict())

@bp.route('/admins', methods=['POST'])
def create_admin():
    data = request.get_json()
    new_admin = Admin(
        username=data['username'],
        password=data['password']
    )
    db.session.add(new_admin)
    db.session.commit()
    return jsonify(new_admin.to_dict()), 201

@bp.route('/admins/<int:admin_id>', methods=['PUT'])
def update_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    data = request.get_json()
    admin.username = data.get('username', admin.username)
    admin.password = data.get('password', admin.password)
    db.session.commit()
    return jsonify(admin.to_dict())

@bp.route('/admins/<int:admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    db.session.delete(admin)
    db.session.commit()
    return '', 204
