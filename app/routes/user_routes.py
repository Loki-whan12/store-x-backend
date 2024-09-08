from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db

user_bp = Blueprint('user_bp', __name__)

# Get all users
@user_bp.route('/get-all-users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# Get user by user_id
@user_bp.route('/get-user-by-id/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user.to_dict()), 200

# Get user by username
@user_bp.route('/get-user-by-username/<string:username>', methods=['GET'])
def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user.to_dict()), 200

# Create a new user
@user_bp.route('/add-users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # Check if username already exists
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({'error': 'Username is already taken'}), 400
    
    # If username is unique, create new user
    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        username=data['username'],
        email=data['email'],
        password=data['password']
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(new_user.to_dict()), 201


# Update a user
# Update a user by username
@user_bp.route('/update-user/<string:username>', methods=['PUT'])
def update_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    data = request.get_json()

    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)

    db.session.commit()
    return jsonify(user.to_dict())


# Delete a user by id
@user_bp.route('/delete-user-by-id/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

# Delete a user by username
@user_bp.route('/delete-user-by-username/<string:username>', methods=['DELETE'])
def delete_user_by_username(username):
    user = User.query.filter_by(username=username).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return '', 204
