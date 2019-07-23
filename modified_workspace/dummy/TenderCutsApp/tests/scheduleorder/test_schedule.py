import pytest
from pytest_bdd import given, scenario, then, when
import pages


@scenario('test_schedule.feature', 'schedule order card')
def test_scheduleordercard():
    """schedule order placing via card"""
    pass


@scenario('test_schedule.feature', 'schedule order cod')
def test_scheduleordercod():
    """Schedule order placing via cod"""
    pass


@pytest.fixture()
def cache():
    return {}


@given('a username <username> and password <password>')
def a_username_and_password(username, password, driver):
    """a username <username> and <password> """
    loginscreen = pages.SignInPage(driver)
    loginscreen.enter_username(username)
    loginscreen.enter_password(password)


@given('when a user click login button it redirect to location page')
def a_user_click_login_button(driver):
    loginscreen = pages.SignInPage(driver)
    loginscreen.submit()
    


@given('enter the location name')
def enter_the_location(driver):
    """enter <location> """
    locationscreen = pages.AddressPage(driver)
    locationscreen.select_existing_address()


@given('when a user select location option it redirect to category page')
def a_user_select_location_option_it_redirect_to_category_page(driver):
    locationscreen = pages.AddressPage(driver)
    locationscreen.verify_categorypage()
    
@given('click category product image chicken it redirect to tcuts product page')
def click_category_product_image_chicken(driver):
    categoryscreen = pages.Homepage(driver)
    categoryscreen.click_categorychicken()
    categoryscreen.verify_tcutspage()


@given('click add button <quantity> from kolaurudai <product> product')
def click_add_button_from_chickencurrycut_product(product, quantity, driver):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.click_product_add(product)
    tcutproductpage.add_one(quantity)


@given('check proceed option enable')
def proceed_option_enable(driver):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.verify_proceedbutton()


@given('click proceed button it redirect to cartsummary page')
def click_proceed_button_it_redirect_to_cartsummary_page(driver):
    proceed = pages.CartSummaryPage(driver)
    proceed.click_proceed()


@given('click checkout button it redirect to deliverysummary page')
def click_checkout_button_it_redirect_to_deliverysummary_page(driver):
    cartpage = pages.CartSummaryPage(driver)
    cartpage.click_checkout()
    cartpage.verify_deliverypage()


@given('select time slot and delivery address <product>')
def select_time_slot_and_delivery_address(product, driver):
    deliveysummarypage = pages.DeliverySummaryPage(driver)
    deliveysummarypage.select_timeslot(product)
    deliveysummarypage.select_address()


@given('when a user click continue button it redirect to payment page')
def a_user_click_continue_button_it_redirect_to_payment_page(driver):
    deliveysummarypage = pages.DeliverySummaryPage(driver)
    deliveysummarypage.click_continue()
    deliveysummarypage.verify_paymentpage()


@given('a user card and enter cvv number')
def select_card_and_enter_cvv_number(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_card()


@when("a user click place order button it redirect to bank page")
def bank_page(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_place_order()


@when('a user click success button from razor payment')
def click_success_button(cache, driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.card_success()
    order_id = paymentpage.get_orderno()
    cache['order_id'] = order_id


@then('verify the order placed in magento <ordertype> <paymenttype>')
def verify(cache, ordertype, paymenttype, driver):
    verify = pages.Verifymagento(driver)
    order_id = cache['order_id']
    # verify.sales_ordercard(order_id, ordertype, paymenttype)


@given('select a cash on delivery option')
def select_cash_on_delivery_option(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_cod()


@when('a user click place order button it redirect to continue shopping page')
def a_user_click_place_order_button_it_redirect_to_continue_shopping_page(cache, driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_place_order()
    order_id = paymentpage.get_orderno()
    cache['order_id'] = order_id
