from flask import Blueprint, request, jsonify
from app import db
from app.models.product import Product

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict()), 200

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if 'name' not in data or 'price' not in data:
        return jsonify({'message': 'Name and price are required'}), 400
    
    new_product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        category_id=data.get('category_id'),
        seller_id=data.get('seller_id')
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    
    if 'name' in data:
        product.name = data['name']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = data['price']
    if 'category_id' in data:
        product.category_id = data['category_id']
    if 'seller_id' in data:
        product.seller_id = data['seller_id']
    
    db.session.commit()
    return jsonify(product.to_dict()), 200

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return '', 204
