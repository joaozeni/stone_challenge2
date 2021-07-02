from apis.models.model import db


class taxi_ride(db.Model):
    __tablename__ = 'taxi_rides'

    id = db.Column(db.BigInteger, primary_key=True)
    vendor_code = db.Column(db.BigInteger, db.ForeignKey('vendors.id'))
    pickup_time = db.Column(db.DateTime)
    dropoff_time = db.Column(db.DateTime)
    ride_time = db.Column(db.Interval) # added for fast use, calculated during the upload
    passenger_count = db.Column(db.Integer)
    trip_distance = db.Column(db.Float)
    pickup_latitude = db.Column(db.Float)
    pickup_longitude = db.Column(db.Float)
    dropoff_latitude = db.Column(db.Float)
    dropoff_longitude = db.Column(db.Float)
    #rate_code = db.Cloumn(db.Float) #ver
    #store_and_fwd_flag = db.Cloumn(db.Float) #ver
    payment_type = db.Column(db.BigInteger, db.ForeignKey('payment_types.id'))
    fare_amount = db.Column(db.Float)
    surcharge_amount = db.Column(db.Float)
    tip_amount = db.Column(db.Float)
    tolls_amount = db.Column(db.Float)
    total_amount = db.Column(db.Float)

