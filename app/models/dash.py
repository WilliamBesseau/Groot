from app.models import db
from app.models.air import Air
from app.models.led import Led
from app.models.moisture import Moisture


class Dash(db.Model):
    __tablename__ = 'dash'

    id = db.Column(db.Integer, primary_key=True)

    temp_value = db.Column(db.Integer)
    temp_status = db.Column(db.String)
    hum_value = db.Column(db.Integer)
    hum_status = db.Column(db.String)

    id_air = db.Column(db.Integer, db.ForeignKey(Air.id, name="fk_assigned_air_id"))
    air = db.relationship('Air', lazy='joined')

    id_led = db.Column(db.Integer, db.ForeignKey(Led.id, name="fk_assigned_led_id"))
    led = db.relationship('Led', lazy='joined')

    id_moisture = db.Column(db.Integer, db.ForeignKey(Moisture.id, name="fk_assigned_moisture_id"))
    moisture = db.relationship('Moisture', lazy='joined')


