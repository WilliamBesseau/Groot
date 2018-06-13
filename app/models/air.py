from app.models import db


class Air(db.Model):
    __tablename__ = 'air'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    value = db.Column(db.Integer)
    status = db.Column(db.String)
