from app import db
from datetime import datetime

class AdminNotification(db.Model):
    __tablename__ = 'admin_notifications'
    notification_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admins.admin_id'))
    notification_type = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text)
    read_status = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    admin = db.relationship('Admin', backref='notifications')
