import pytest
from pytest_bdd import given, scenario, then, when
import pages
import time


@scenario('test_searchoption.feature', 'place order via search option')
def test_searchoption():
    """Express order placing via card"""
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


@when('a user click login button it redirect to location page')
def a_user_click_login_button(driver):
    loginscreen = pages.SignInPage(driver)
    loginscreen.submit()


@then('enter the location name')
def enter_the_location(driver):
    """enter <location> """
    locationscreen = pages.AddressPage(driver)
    locationscreen.select_existing_address()


@then('when a user select location option it redirect to category page')
def a_user_select_location_option_it_redirect_to_category_page(driver):
    locationscreen = pages.AddressPage(driver)
    locationscreen.verify_categorypage()


@then('click category product image chicken it redirect to tcuts product page')
def click_category_product_image_chicken(driver):
    categoryscreen = pages.Homepage(driver)
    categoryscreen.click_categorychicken()
    categoryscreen.verify_tcutspage()


@then("click add button <quantity> from chickencurrycut <product> product")
def click_add_button_from_chickencurrycut_product(product, quantity, driver):
    tcutproductpage = pages.Categorypage(driver)
    # tcutproductpage.click_product_add(product)
    # tcutproductpage.add_one(quantity)


@then('check proceed option enable')
def proceed_option_enable(driver):
    tcutproductpage = pages.Categorypage(driver)
    # tcutproductpage.verify_proceedbutton()


@then('click proceed button it redirect to cartsummary page')
def click_proceed_button_it_redirect_to_cartsummary_page(driver):
    proceed = pages.CartSummaryPage(driver)
    proceed.click_proceed_search()


@then('click checkout button it redirect to deliverysummary page')
def click_checkout_button_it_redirect_to_deliverysummary_page(driver):
    cartpage = pages.CartSummaryPage(driver)
    cartpage.click_checkout()
    cartpage.verify_deliverypage()


@then('select time slot and delivery address <product>')
def select_time_slot_and_delivery_address(product, driver):
    deliveysummarypage = pages.DeliverySummaryPage(driver)
    deliveysummarypage.select_timeslot(product)
    deliveysummarypage.select_address()


@then('when a user click continue button it redirect to payment page')
def a_user_click_continue_button_it_redirect_to_payment_page(driver):
    deliveysummarypage = pages.DeliverySummaryPage(driver)
    deliveysummarypage.click_continue()
    deliveysummarypage.verify_paymentpage()


@then('verify the order placed in magento <ordertype> <paymenttype>')
def verify(cache, ordertype, paymenttype, driver):
    verify = pages.Verifymagento(driver)
    orderid = cache['order_id']
    # verify.sales_ordercard(orderid, ordertype, paymenttype)


@then('select a cash on delivery option')
def select_cash_on_delivery_option(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_cod()


@then('a user click place order button it redirect to continue shopping page')
def a_user_click_place_order_button_it_redirect_to_continue_shopping_page(cache, driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_place_order()
    orderid = paymentpage.get_orderno()
    cache['order_id'] = orderid


@then('click the search option and enter product name')
def click_the_search_option(driver):
    searchpage = pages.SearchPage(driver)
    searchpage.click_search()
    searchpage.enter_chickenproduct()
    searchpage.click_addbutton()
