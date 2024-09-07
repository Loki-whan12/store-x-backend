from app import db
from datetime import datetime

class DeletedProduct(db.Model):
    __tablename__ = 'deleted_products'
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    category_id = db.Column(db.Integer)
    seller_id = db.Column(db.Integer)
    deleted_reason = db.Column(db.Text)
    deleted_at = db.Column(db.DateTime, default=datetime.utcnow)
