import time
import pytest
from appium import webdriver
from pytest_bdd import given, scenario, then, when
import lib
import pages_custom


@scenario('test_expressorder.feature', 'placing order card')
def test_expressordercard():
    """Express order placing via card"""
    pass


@scenario('test_expressorder.feature', 'placing order cod')
def test_expressorder_cod():
    """Express order placing via cod"""
    pass

@scenario('test_expressorder.feature', 'placing order cod for egg')
def test_expressordercodegg():
    """Express order placing via cod"""
    pass

@scenario('test_expressorder.feature', 'placing order cod for pickle')
def test_expressordercodpickle():
    """Express order placing via cod"""
    pass


@pytest.fixture()
def cache():
    return {}


@given('a username <username> and password <password>')
def a_username_and_password(username, password, driver):
    """a username <username> and <password> """
    loginscreen = pages_custom.SignInPage(driver)
    loginscreen.enter_username(username)
    loginscreen.enter_password(password)


@given('when a user click login button it redirect to location page')
def a_user_click_login_button(driver):
    loginscreen = pages_custom.SignInPage(driver)
    loginscreen.submit()


@given('enter the location name')
def enter_the_location(driver):
    """enter <location> """
    locationscreen = pages_custom.AddressPage(driver)
    locationscreen.select_existing_address()


@given('when a user select location option it redirect to category page')
def a_user_select_location_option_it_redirect_to_category_page(driver):
    locationscreen = pages_custom.AddressPage(driver)
    locationscreen.verify_categorypage()


@given('click category product image chicken it redirect to tcuts product page')
def click_category_product_image_chicken(driver):
    categoryscreen = pages_custom.Homepage(driver)
    categoryscreen.click_categorychicken()
    categoryscreen.verify_tcutspage()


@given("click add button <quantity> from chickencurrycut <product> product")
def click_add_button_from_chickencurrycut_product(product, quantity, driver):
    tcutproductpage = pages_custom.Categorypage(driver)
    tcutproductpage.click_product_add(product)
    tcutproductpage.add_one(quantity)


@given('check proceed option enable')
def proceed_option_enable(driver):
    tcutproductpage = pages_custom.Categorypage(driver)
    tcutproductpage.verify_proceedbutton()


@given('click proceed button it redirect to cartsummary page')
def click_proceed_button_it_redirect_to_cartsummary_page(driver):
    proceed = pages_custom.CartSummaryPage(driver)
    proceed.click_proceed()


@given('click checkout button it redirect to deliverysummary page')
def click_checkout_button_it_redirect_to_deliverysummary_page(driver):
    cartpage = pages_custom.CartSummaryPage(driver)
    cartpage.click_checkout()
    cartpage.verify_deliverypage()


@given('select time slot and delivery address <product>')
def select_time_slot_and_delivery_address(product, driver):
    deliveysummarypage = pages_custom.DeliverySummaryPage(driver)
    deliveysummarypage.select_timeslot(product)
    deliveysummarypage.select_address()


@given('when a user click continue button it redirect to payment page')
def a_user_click_continue_button_it_redirect_to_payment_page(driver):
    deliveysummarypage = pages_custom.DeliverySummaryPage(driver)
    deliveysummarypage.click_continue()
    deliveysummarypage.verify_paymentpage()


@given('a user card and enter cvv number')
def select_card_and_enter_cvv_number(driver):
    paymentpage = pages_custom.PaymentPage(driver)
    paymentpage.click_card()


@when("a user click place order button it redirect to bank page")
def bank_page(driver):
    paymentpage = pages_custom.PaymentPage(driver)
    paymentpage.click_place_order()


@when('a user click success button from razor payment')
def click_success_button(cache, driver):
    paymentpage = pages_custom.PaymentPage(driver)
    paymentpage.card_success()
    orderid = paymentpage.get_orderno()
    cache['order_id'] = orderid


@then('verify the order placed in magento <ordertype> <paymenttype>')
def verify(cache, ordertype, paymenttype, driver):
    orderid = cache['order_id']
    # verify = pages.Verifymagento(driver)
    # verify.sales_ordercard(orderid, ordertype, paymenttype)


@given('select a cash on delivery option')
def select_cash_on_delivery_option(driver):
    paymentpage = pages_custom.PaymentPage(driver)
    paymentpage.click_cod()


@when('a user click place order button it redirect to continue shopping page')
def a_user_click_place_order_button_it_redirect_to_continue_shopping_page(cache, driver):
    paymentpage = pages_custom.PaymentPage(driver)
    paymentpage.click_place_order()
    orderid=paymentpage.get_orderno()
    cache['order_id'] = orderid
