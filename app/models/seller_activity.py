from app import db
from datetime import datetime

class SellerActivity(db.Model):
    __tablename__ = 'seller_activities'
    activity_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.seller_id'))
    activity_type = db.Column(db.String(100), nullable=False)
    activity_details = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    seller = db.relationship('Seller', backref='activities')
