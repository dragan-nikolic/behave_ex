import requests

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

    if response.status_code != 200:
        raise ResponseError(
            "Incorrect status code: {} ({})".format(
                response.status_code,
                response.reason))

    return [x['bookingid'] for x in response.json()]

def get_booking_by_id(id):
    response = requests.get(_url("/booking/{}".format(id)))

    if response.status_code != 200:
        raise ResponseError(
            "Incorrect status code: {} ({})".format(
                response.status_code,
                response.reason))

    return response.json()
