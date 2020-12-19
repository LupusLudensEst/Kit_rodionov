from behave import *

@then("Click on Ekaterinburg/Moscow")
def clck_mosc_is_hr(context):
    """
    Enter the main page and verify https://ekaterinburg.gtdel.com/ is here
    """
    context.app.main_page.clck_mosc_is_hr()


@step('Verify "https://moscow.gtdel.com/" is here')
def mosc_url_is_here(context):
    """
    Verify "https://moscow.gtdel.com/" is here
    """
    context.app.main_page.mosc_url_is_here()