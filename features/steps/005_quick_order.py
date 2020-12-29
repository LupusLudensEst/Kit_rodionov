from behave import *

@then('Click on "ЗАКАЗАТЬ"')
def click_on_order(context):
    """
    Click on "ЗАКАЗАТЬ"
    """
    context.app.main_page.click_on_order()


@step('Click on "от терминала"')
def click_on_from_terminal(context):
    """
    Click on "от терминала"
    """
    context.app.main_page.click_on_from_terminal()


@then('Click on "до терминала"')
def click_on_to_terminal(context):
    """
    Click on "до терминала"
    """
    context.app.main_page.click_on_to_terminal()


@step('Send "{kgs}" to "кг"')
def send_weight(context, kgs):
    """
    Send "999" to "кг"
    """
    context.app.main_page.send_weight(kgs)


@then('Send "{volume}" to "м3"')
def send_volume(context, volume):
    """
    Send "3.500" to "м3"
    """
    context.app.main_page.send_volume(volume)


@step('Send "{places}" to "мест"')
def send_places(context, places):
    """
    Send "3" to "мест"
    """
    context.app.main_page.send_places(places)


@then('Send "{goods_value}" to "₽"')
def send_goods_value(context, goods_value):
    """
    Send "30000" to "₽"
    """
    context.app.main_page.send_goods_value(goods_value)


@step('Click on "рассчитать"')
def click_count(context):
    """
    Click on "рассчитать"
    """
    context.app.main_page.click_count()


@then('Verify "4 дня" is here as text')
def days_are_here(context):
    """
    Verify "4 дня" is here as text'
    """
    context.app.main_page.days_are_here()


@step('Verify "8 941 ₽/8&nbsp;941 ₽" is here as text')
def freight_cost_is_here(context):
    """
    Verify "8 941 ₽/8&nbsp;941 ₽" is here as text
    """
    context.app.main_page.freight_cost_is_here()