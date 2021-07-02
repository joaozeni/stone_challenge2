
from apis.models.model import db


class vendor(db.Model):
    __tablename__ = 'vendors'

    id = db.Column(db.BigInteger, primary_key=True)
    vendor_code = db.Column(db.String(3))
    name = db.Column(db.String(128))
    address = db.Column(db.String(128))
    city = db.Column(db.String(128))
    state = db.Column(db.String(128))
    zip_code = db.Column(db.String(128))
    country = db.Column(db.String(128))
    contact = db.Column(db.String(128))
    current = db.Column(db.Boolean)

