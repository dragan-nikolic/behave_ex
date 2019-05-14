import requests

def _url(path):
    return 'https://restful-booker.herokuapp.com' + path

def get_bookings(firstname="", lastname="", checkin="", checkout=""):
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
        return requests.get(_url('/booking/'), params=payload)
    else:
        return requests.get(_url('/booking/'))

@when(u'I request Mark\'s booking')
def step_impl(context):
    resp = get_bookings('Mark')
    print(resp.json())

@then(u'I should receive Mark\'s booking info')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should receive Mark\'s booking info')
