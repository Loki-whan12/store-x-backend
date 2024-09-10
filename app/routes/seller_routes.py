from flask import Blueprint, request, jsonify
from app import db
from app.models.seller import Seller
from app.models.user import User  # Import the User model for username-based queries

seller_bp = Blueprint('seller_bp', __name__)

# Route to get all sellers
# GET /sellers
@seller_bp.route('/get-all-sellers', methods=['GET'])
def get_sellers():
    # Fetch all sellers from the database
    sellers = Seller.query.all()
    # Return a list of sellers in JSON format
    return jsonify([seller.to_dict() for seller in sellers]), 200

# Route to get a specific seller by username
# GET /sellers/username/<username>
@seller_bp.route('/sellers/username/<string:username>', methods=['GET'])
def get_seller_by_username(username):
    # Fetch a seller by username or return a 404 if not found
    seller = Seller.query.filter_by(username=username).first_or_404()
    # Return the seller details in JSON format
    return jsonify(seller.to_dict()), 200

# Route to create a new seller
# POST /sellers
@seller_bp.route('/add-seller', methods=['POST'])
def create_seller():
    # Parse JSON data from the request
    data = request.get_json()

    # Check if the required fields are provided
    if 'username' not in data or 'seller_name' not in data or 'password' not in data:
        return jsonify({'message': 'Username, seller name, and password are required'}), 400

    # Retrieve the user by username
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Check if a seller with this username already exists
    existing_seller = Seller.query.filter_by(username=data['username']).first()
    if existing_seller:
        return jsonify({'message': 'Seller with this username already exists'}), 400

    # Create a new Seller object with the provided data
    new_seller = Seller(
        seller_id=user.user_id,
        username=data['username'],
        seller_name=data['seller_name'],
        password=data['password'],
        has_been_approved=False
    )

    # Add the new seller to the session and commit it to the database
    db.session.add(new_seller)
    db.session.commit()

    # Return the newly created seller details
    return jsonify(new_seller.to_dict()), 201

# Route to update an existing seller by username
# PUT /sellers/username/<username>
@seller_bp.route('/update-seller/username/<string:username>', methods=['PUT'])
def update_seller_by_username(username):
    # Retrieve the user by username
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    # Fetch the seller using the username or create a new one if not found
    seller = Seller.query.filter_by(username=username).first()
    if seller:
        # Update existing seller attributes if they exist in the request
        data = request.get_json()
        if 'company_name' in data:
            seller.company_name = data['company_name']
        if 'business_license_number' in data:
            seller.business_license_number = data['business_license_number']
        message = 'Seller updated successfully'
    else:
        # Create a new Seller if none exists for the username
        data = request.get_json()
        seller = Seller(
            username=username,
            company_name=data.get('company_name'),
            business_license_number=data.get('business_license_number')
        )
        db.session.add(seller)
        message = 'Seller created successfully'
        
    # Commit the changes to the database
    db.session.commit()
    # Return the seller details along with a message indicating the action taken
    return jsonify({'seller': seller.to_dict(), 'message': message}), 200

# Route to delete a seller by username
# DELETE /sellers/username/<username>
@seller_bp.route('/delete-seller/<string:username>', methods=['DELETE'])
def delete_seller_by_username(username):
    # Fetch the seller by username or return a 404 if not found
    seller = Seller.query.filter_by(username=username).first_or_404()
    # Delete the seller from the database
    db.session.delete(seller)
    db.session.commit()
    return '', 204
