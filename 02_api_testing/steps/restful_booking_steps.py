from support.restful_booking_api import *

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
