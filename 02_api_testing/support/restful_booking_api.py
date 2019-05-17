import requests
import random
from faker import Faker

class ResponseError(Exception):
    pass

def _url(path):
    return 'https://restful-booker.herokuapp.com' + path

def get_booking_ids(
        firstname="", 
        lastname="", 
        checkin="", 
        checkout=""):

    payload = {}

    if firstname:
        payload['firstname'] = firstname
    if lastname:
        payload['lastname'] = lastname
    if checkin:
        payload['checkin'] = checkin
    if checkout:
        payload['checkout'] = checkout

    if payload:
        response = requests.get(_url('/booking/'), params=payload)
    else:
        response = requests.get(_url('/booking/'))

    assert\
        response.status_code == 200,\
        "Incorrect status code: {} ({})".format(
            response.status_code,
            response.reason)

    return [x['bookingid'] for x in response.json()]

def get_booking_by_id(id):
    response = requests.get(_url("/booking/{}".format(id)))

    assert\
        response.status_code == 200,\
        "Incorrect status code: {} ({})".format(
            response.status_code,
            response.reason)

    return response.json()

def create_booking(booking):
    response = requests.post(_url('/booking/'), json=booking)

    assert\
        response.status_code == 200,\
        "Incorrect status code: {} ({})".format(
            response.status_code,
            response.reason)

    return response.json()

def generate_fake_booking():
    fake = Faker()

    return(
        {
            'firstname': fake.first_name(),
            'lastname': fake.last_name(),
            'totalprice': fake.random_number(digits=3, fix_len=True),
            'depositpaid': fake.boolean(),
            'bookingdates': {
                'checkin': str(fake.date_between(start_date='-30d', end_date='-15d')),
                'checkout': str(fake.date_between(start_date='-15d', end_date='today'))
            },
            'additionalneeds': random.choice([
                'Breakfast', 
                'Mini Fridge', 
                'Extra towel', 
                'Dinner'
            ])
        }
    )

def validate(expression, message):
    assert expression, message
