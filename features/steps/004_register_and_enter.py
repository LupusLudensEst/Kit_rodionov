from behave import *

@step("Register as a new user")
def rgstr_as_nw_usr(context):
    """
    Register as a new user
    """
    context.app.main_page.rgstr_as_nw_usr()


@then('Verify text: "{text_here}" is here')
def text_here(context, text_here):
    """
    Verify text: Подтверждение доступа is here
    """
    context.app.main_page.text_here()