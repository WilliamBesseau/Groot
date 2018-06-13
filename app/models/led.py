from app.models import db


class Led(db.Model):
    __tablename__ = 'led'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    value = db.Column(db.Integer)

