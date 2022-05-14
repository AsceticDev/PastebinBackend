from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

from pastebinBackend.extensions import db

class Paste(db.Model):

    __tablename__ = "paste"
    id = db.Column(db.Integer, primary_key=True);
    title = db.Column(db.String(100), nullable=False);
    content = db.Column(db.Text(), nullable=False);
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow);
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # optional
    encrypted = db.Column(db.Boolean, default=False);

    def __repr__(self):
        return f"Paste('{self.title}',{self.createdAt}')"