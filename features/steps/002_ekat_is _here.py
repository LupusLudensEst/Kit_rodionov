from behave import *

@then("Click on Ekaterinburg/Yes")
def clck_ekat_is_hr(context):
    """
    Enter the main page and verify https://ekaterinburg.gtdel.com/ is here
    """
    context.app.main_page.clck_ekat_is_hr()


@step('Verify "https://ekaterinburg.gtdel.com/" is here')
def ek_url_is_here(context):
    """
    Verify "https://ekaterinburg.gtdel.com/" is here
    """
    context.app.main_page.ek_url_is_here()