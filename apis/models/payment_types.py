from apis.models.model import db


class payment_type(db.Model):
    __tablename__ = 'payment_types'

    id = db.Column(db.BigInteger, primary_key=True)
    payment_type = db.Column(db.String(30))
