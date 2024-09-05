from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@given(u'there was a commit with a commit message that is "foo"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given there was a commit with a commit message that is "foo"')


@when(u'we run the log')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we run the log')


@then(u'the log shows an entry with the message that is "foo"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the log shows an entry with the message that is "foo"')
