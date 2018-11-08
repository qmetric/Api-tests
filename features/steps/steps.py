# file:features/steps/steps.py
from behave import *
from classes.quotes import Quotes
from classes.enquiry import Enquiry
from classes.bolt_ons_model import Bolt_ons

@given('the consultant submit an enquiry with "{affiliate}" affiliate')
def step_implement(context, affiliate):
    enquiry_form = Enquiry(context.resource_dir, context.app, "basic_home_enquiry.py", context.header, referrer=affiliate)
    context.transaction = enquiry_form.submit(context.jump_box, context.base_url)


@then('all offered quotes are "{vendor}"')
def step_implement(context, vendor):
        Quotes.is_broker(context.transaction["quotes"], vendor)


@then('some bolt-ons are offered')
def step_impl(context):
    context.bolt_on_setting = Bolt_ons()
    for row in context.table:
    context.bolt_on_setting.add_bolt_on(name=row["Bolt-ons"], price=row["Price"], availabality=row["Available"], selected=row["selected"])
    context.bolt_on_setting.validate_results(context.transaction.get_bolt_ons)



