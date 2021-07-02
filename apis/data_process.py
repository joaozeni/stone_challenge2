from pytz import timezone
import json
from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from sqlalchemy import func, extract, and_
from apis.models.taxi_ride import taxi_ride
from apis.models.vendors import vendor
from apis.models.payment_types import payment_type
from apis.models.model import db


data_process_blueprint = Blueprint('data_process', __name__)


@data_process_blueprint.route('/avg_ride', methods=['GET'])
def avg_distance():

    """Checks if the system is alive
        ---
        responses:
          200:
            description: returns the avarege trip with a maximum of 2 passangers
    """
    query = db.session.query(func.avg(taxi_ride.trip_distance).label('average')).filter(taxi_ride.passenger_count<=2)
    query_results = db.session.execute(query)
    avg = query_results.all()[0][0]
    return {'avarage':avg}, 200


@data_process_blueprint.route('/biggest', methods=['GET'])
def biggest():

    """Checks if the system is alive
        ---
        responses:
          200:
            description: returns the biggest vendors by amount raised
    """
    query = db.session.query(func.sum(taxi_ride.total_amount).label('total_value'), vendor.vendor_code).join(vendor, vendor.id==taxi_ride.vendor_code).group_by(vendor.vendor_code)
    query_results = db.session.execute(query)
    biggest = query_results.all()
    biggest_dict = dict()
    biggest_dict[biggest[0][1]] = biggest[0][0]
    biggest_dict[biggest[1][1]] = biggest[1][0]
    biggest_dict[biggest[2][1]] = biggest[2][0]
    return {'biggest':biggest_dict}, 200


@data_process_blueprint.route('/rides_with_cash', methods=['GET'])
def rides_with_cash():

    """Checks if the system is alive
        ---
        responses:
          200:
            description: return rides month-by-month with cash
    """
    query = db.session.query(func.count(taxi_ride.id).label('number_of_rides'),extract('month', taxi_ride.pickup_time),extract('year', taxi_ride.pickup_time)).join(payment_type, payment_type.id==taxi_ride.payment_type).group_by(extract('month', taxi_ride.pickup_time), extract('year', taxi_ride.pickup_time)).filter(payment_type.payment_type=='Cash')
    query_results = db.session.execute(query)
    rides_dict = dict()
    for item in query_results:
        month = int(item[1])
        year = int(item[2])
        index = f'{month}/{year}'
        rides_dict[index] = item[0]
    return {'histogram':rides_dict}, 200


@data_process_blueprint.route('/tips', methods=['GET'])
def tips():

    """Checks if the system is alive
        ---
        responses:
          200:
            description: return rides month-by-month with cash
    """
    query = db.session.query(func.count(taxi_ride.tip_amount).label('number_of_tips'),extract('month', taxi_ride.pickup_time),extract('day', taxi_ride.pickup_time)).group_by(extract('month', taxi_ride.pickup_time), extract('day', taxi_ride.pickup_time)).filter(extract('year', taxi_ride.pickup_time) == 2012).filter(extract('month', taxi_ride.pickup_time) >= 10)
    query_results = db.session.execute(query)
    tips_dict = dict()
    for item in query_results:
        month = int(item[1])
        day = int(item[2])
        index = f'{day}/{month}'
        tips_dict[index] = item[0]
    return {'tips':tips_dict}, 200
