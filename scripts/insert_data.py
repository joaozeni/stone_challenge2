from pytz import timezone
import pandas
import psycopg2
from datetime import datetime
from dateutil import parser
import json

try:
    conn = psycopg2.connect("dbname='taxi_rides_db' user='postgres' password='postgres' host='localhost'")
except:
    print("DB connection failed.")
    quit()

cur = conn.cursor()

vendors = pandas.read_csv('data-vendor_lookup-csv.csv', header=0)

print('Inserindo operadores')
local_time = timezone('Etc/GMT-3')
vendor_id = 1
vendors_dict = dict()
for index, vendor in vendors.iterrows():
    id = vendor_id
    vendor_code = vendor['vendor_id']
    vendor_name = vendor['name']
    vendor_address = vendor['address']
    vendor_city = vendor['city']
    vendor_state = vendor['state']
    vendor_zip = vendor['zip']
    vendor_country = vendor['country']
    vendor_contact = vendor['contact']
    vendor_current = bool(vendor['current'])
    cur.execute(f"INSERT INTO vendors (id, vendor_code, name, address, city, state, zip_code, country, contact, current) VALUES ({id}, '{vendor_code}', '{vendor_name}', '{vendor_address}', '{vendor_city}', '{vendor_state}', '{vendor_zip}', '{vendor_country}', '{vendor_contact}', '{vendor_current}')")
    vendors_dict[vendor_code] = vendor_id
    vendor_id += 1

conn.commit()

payment_types = pandas.read_csv('data-payment_lookup-csv.csv', header=0)
payments_dict = dict()
id_mapper = dict()
payment_id = 1

print('Inserindo tipos de pagamento')
for index, item in payment_types.iterrows():
    code = item['A']
    payment = item['B']
    if payment not in payments_dict.keys():
        cur.execute(f"INSERT INTO payment_types (id, payment_type) VALUES ({payment_id}, '{payment}')")
        payments_dict[payment] = payment_id
        id_mapper[code] = payment_id
        payment_id += 1
    else:
        id_mapper[code] = payments_dict[payment]

conn.commit()

print('Inserindo corridas 2009')
ride_id = 1
with open('data-sample_data-nyctaxi-trips-2009-json_corrigido.json') as f:
    for jsonObj in f:
        ride = json.loads(jsonObj)
        id = ride_id 
        vendor_code = vendors_dict[ride['vendor_id']]
        pickup_time = parser.parse(ride['pickup_datetime'])
        dropoff_time = parser.parse(ride['dropoff_datetime'])
        ride_time = dropoff_time-pickup_time
        passenger_count = ride['passenger_count']
        trip_distance = ride['trip_distance']
        pickup_latitude = ride['pickup_longitude']
        pickup_longitude = ride['pickup_latitude']
        dropoff_latitude = ride['dropoff_longitude']
        dropoff_longitude = ride['dropoff_latitude']
        payment_type = id_mapper[ride['payment_type']]
        fare_amount = ride['fare_amount']
        surcharge_amount = ride['surcharge']
        tip_amount = ride['tip_amount']
        tolls_amount = ride['tolls_amount']
        total_amount = ride['total_amount'] 
        cur.execute(f"INSERT INTO taxi_rides (id, vendor_code, pickup_time, dropoff_time, ride_time, passenger_count, trip_distance, pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude, payment_type, fare_amount, surcharge_amount, tip_amount, tolls_amount, total_amount) VALUES ({id}, '{vendor_code}', '{pickup_time}', '{dropoff_time}', '{ride_time}', {passenger_count}, {trip_distance}, {pickup_latitude}, {pickup_longitude}, {dropoff_latitude}, {dropoff_longitude}, {payment_type}, {fare_amount}, {surcharge_amount}, {tip_amount}, {tolls_amount}, {total_amount})")
        ride_id += 1

conn.commit()

print('Inserindo corridas 2010')
with open('data-sample_data-nyctaxi-trips-2010-json_corrigido.json') as f:
    for jsonObj in f:
        ride = json.loads(jsonObj)
        id = ride_id 
        vendor_code = vendors_dict[ride['vendor_id']]
        pickup_time = parser.parse(ride['pickup_datetime'])
        dropoff_time = parser.parse(ride['dropoff_datetime'])
        ride_time = dropoff_time-pickup_time
        passenger_count = ride['passenger_count']
        trip_distance = ride['trip_distance']
        pickup_latitude = ride['pickup_longitude']
        pickup_longitude = ride['pickup_latitude']
        dropoff_latitude = ride['dropoff_longitude']
        dropoff_longitude = ride['dropoff_latitude']
        payment_type = id_mapper[ride['payment_type']]
        fare_amount = ride['fare_amount']
        surcharge_amount = ride['surcharge']
        tip_amount = ride['tip_amount']
        tolls_amount = ride['tolls_amount']
        total_amount = ride['total_amount'] 
        cur.execute(f"INSERT INTO taxi_rides (id, vendor_code, pickup_time, dropoff_time, ride_time, passenger_count, trip_distance, pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude, payment_type, fare_amount, surcharge_amount, tip_amount, tolls_amount, total_amount) VALUES ({id}, '{vendor_code}', '{pickup_time}', '{dropoff_time}', '{ride_time}', {passenger_count}, {trip_distance}, {pickup_latitude}, {pickup_longitude}, {dropoff_latitude}, {dropoff_longitude}, {payment_type}, {fare_amount}, {surcharge_amount}, {tip_amount}, {tolls_amount}, {total_amount})")
        ride_id += 1

conn.commit()

print('Inserindo corridas 2011')
with open('data-sample_data-nyctaxi-trips-2011-json_corrigido.json') as f:
    for jsonObj in f:
        ride = json.loads(jsonObj)
        id = ride_id 
        vendor_code = vendors_dict[ride['vendor_id']]
        pickup_time = parser.parse(ride['pickup_datetime'])
        dropoff_time = parser.parse(ride['dropoff_datetime'])
        ride_time = dropoff_time-pickup_time
        passenger_count = ride['passenger_count']
        trip_distance = ride['trip_distance']
        pickup_latitude = ride['pickup_longitude']
        pickup_longitude = ride['pickup_latitude']
        dropoff_latitude = ride['dropoff_longitude']
        dropoff_longitude = ride['dropoff_latitude']
        payment_type = id_mapper[ride['payment_type']]
        fare_amount = ride['fare_amount']
        surcharge_amount = ride['surcharge']
        tip_amount = ride['tip_amount']
        tolls_amount = ride['tolls_amount']
        total_amount = ride['total_amount'] 
        cur.execute(f"INSERT INTO taxi_rides (id, vendor_code, pickup_time, dropoff_time, ride_time, passenger_count, trip_distance, pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude, payment_type, fare_amount, surcharge_amount, tip_amount, tolls_amount, total_amount) VALUES ({id}, '{vendor_code}', '{pickup_time}', '{dropoff_time}', '{ride_time}', {passenger_count}, {trip_distance}, {pickup_latitude}, {pickup_longitude}, {dropoff_latitude}, {dropoff_longitude}, {payment_type}, {fare_amount}, {surcharge_amount}, {tip_amount}, {tolls_amount}, {total_amount})")
        ride_id += 1

conn.commit()


print('Inserindo corridas 2012')
with open('data-sample_data-nyctaxi-trips-2012-json_corrigido.json') as f:
    for jsonObj in f:
        ride = json.loads(jsonObj)
        id = ride_id 
        vendor_code = vendors_dict[ride['vendor_id']]
        pickup_time = parser.parse(ride['pickup_datetime'])
        dropoff_time = parser.parse(ride['dropoff_datetime'])
        ride_time = dropoff_time-pickup_time
        passenger_count = ride['passenger_count']
        trip_distance = ride['trip_distance']
        pickup_latitude = ride['pickup_longitude']
        pickup_longitude = ride['pickup_latitude']
        dropoff_latitude = ride['dropoff_longitude']
        dropoff_longitude = ride['dropoff_latitude']
        payment_type = id_mapper[ride['payment_type']]
        fare_amount = ride['fare_amount']
        surcharge_amount = ride['surcharge']
        tip_amount = ride['tip_amount']
        tolls_amount = ride['tolls_amount']
        total_amount = ride['total_amount'] 
        cur.execute(f"INSERT INTO taxi_rides (id, vendor_code, pickup_time, dropoff_time, ride_time, passenger_count, trip_distance, pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude, payment_type, fare_amount, surcharge_amount, tip_amount, tolls_amount, total_amount) VALUES ({id}, '{vendor_code}', '{pickup_time}', '{dropoff_time}', '{ride_time}', {passenger_count}, {trip_distance}, {pickup_latitude}, {pickup_longitude}, {dropoff_latitude}, {dropoff_longitude}, {payment_type}, {fare_amount}, {surcharge_amount}, {tip_amount}, {tolls_amount}, {total_amount})")
        ride_id += 1

conn.commit()

cur.close()
conn.close()
