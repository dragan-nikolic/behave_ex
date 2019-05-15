import requests

class ResponseError(Exception):
    pass

class ValidationError(Exception):
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

    if response.status_code != 200:
        raise ResponseError(
            "Incorrect status code: {} ({})".format(
                response.status_code,
                response.reason))

    return [x['bookingid'] for x in response.json()]

def get_booking(id):
    response = requests.get(_url("/booking/{}".format(id)))

    if response.status_code != 200:
        raise ResponseError(
            "Incorrect status code: {} ({})".format(
                response.status_code,
                response.reason))

    return response.json()

@when(u'I request Mark\'s booking')
def step_impl(context):
    context.user = 'Mark'
    context.booking_ids = get_booking_ids(context.user)

@then(u'I should receive Mark\'s booking info')
def step_impl(context):
    for booking_id in context.booking_ids:
        booking_info = get_booking(booking_id)
        if booking_info['firstname'] != context.user:
            raise ValidationError(
                "Incorrect user: {}".format(booking_info['firstname']))
