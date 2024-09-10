from app import db
from datetime import datetime
from app.models.user import User


class Seller(db.Model):
    __tablename__ = 'sellers'
    seller_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), unique=True, nullable=False)
    username = db.Column(db.String(50), db.ForeignKey('users.username'), unique=True, nullable=False)
    seller_name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Establishing a relationship with the User model
    user = db.relationship('User', backref='seller', uselist=False)

    def to_dict(self):
        return {
            'seller_id': self.seller_id,
            'user_id': self.user_id,
            'username': self.username,
            'seller_name': self.seller_name,
            'password': self.password,
            'created_at': self.created_at,
            'updated_at': self.updated_at
    }