from flask_migrate import Migrate

from apis.app import create_app
from apis.models.model import db
from apis.models.payment_types import payment_type
from apis.models.taxi_ride import taxi_ride
from apis.models.vendors import vendor

app = create_app()
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, taxi_ride=taxi_ride, vendor=vendor, payment_type=payment_type)


#if __name__ == '__main__':
#    make_shell_context()[app].run(host="0.0.0.0", port='5000', debug=True)
