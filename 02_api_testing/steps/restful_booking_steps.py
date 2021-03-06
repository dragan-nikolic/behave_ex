from support.restful_booking_api import *

@when(u'I request Mark\'s bookings')
def step_impl(context):
    context.user = 'Mark'
    context.booking_ids = get_booking_ids(context.user)

@then(u'I should receive Mark\'s bookings info')
def step_impl(context):
    for booking_id in context.booking_ids:
        booking_info = get_booking_by_id(booking_id)
        assert\
            booking_info['firstname'] == context.user,\
            "Got info for incorrect user: {}!".format(booking_info['firstname'])

@when(u'I add new booking')
def step_impl(context):
    context.booking = generate_fake_booking()
    response = create_booking(context.booking)
    context.booking_id = response['bookingid']

@then(u'I should see new booking in the list')
def step_impl(context):
    booking = get_booking_by_id(context.booking_id)

    validate(
        booking == context.booking,
        "Could not find just generated booking!\n"
            "Expected: {}\nActual: {}".format(context.booking, booking))
