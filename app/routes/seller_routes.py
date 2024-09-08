from flask import Blueprint, request, jsonify
from app import db
from app.models.seller import Seller

seller_bp = Blueprint('seller_bp', __name__)

@seller_bp.route('/sellers', methods=['GET'])
def get_sellers():
    sellers = Seller.query.all()
    return jsonify([seller.to_dict() for seller in sellers]), 200

@seller_bp.route('/sellers/<int:seller_id>', methods=['GET'])
def get_seller(seller_id):
    seller = Seller.query.get_or_404(seller_id)
    return jsonify(seller.to_dict()), 200

@seller_bp.route('/sellers', methods=['POST'])
def create_seller():
    data = request.get_json()
    if 'user_id' not in data:
        return jsonify({'message': 'User ID is required'}), 400
    new_seller = Seller(
        user_id=data['user_id'],
        company_name=data.get('company_name'),
        business_license_number=data.get('business_license_number')
    )
    db.session.add(new_seller)
    db.session.commit()
    return jsonify(new_seller.to_dict()), 201

@seller_bp.route('/sellers/<int:seller_id>', methods=['PUT'])
def update_seller(seller_id):
    seller = Seller.query.get_or_404(seller_id)
    data = request.get_json()
    if 'company_name' in data:
        seller.company_name = data['company_name']
    if 'business_license_number' in data:
        seller.business_license_number = data['business_license_number']
    db.session.commit()
    return jsonify(seller.to_dict()), 200

@seller_bp.route('/sellers/<int:seller_id>', methods=['DELETE'])
def delete_seller(seller_id):
    seller = Seller.query.get_or_404(seller_id)
    db.session.delete(seller)
    db.session.commit()
    return '', 204
