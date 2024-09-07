from app import db
from datetime import datetime

class SellerNotification(db.Model):
    __tablename__ = 'seller_notifications'
    notification_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.seller_id'))
    notification_type = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text)
    read_status = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    seller = db.relationship('Seller', backref='notifications')

    