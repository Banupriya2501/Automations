import time
import pytest
from appium import webdriver
from pytest_bdd import given, scenario, then, when
import lib
import pages
import MySQLdb
import datetime



# @scenario('test_storecredit.feature', 'auto select cod')
# def test_autocod():
#     """"place order with storecredit auto select cod"""
#     pass

@scenario('test_storecredit.feature', 'store credit with cod')
def test_storecreditcod():
    """"place order with storecredit with cod"""
    pass

@scenario('test_storecredit.feature', 'store credit with card')
def test_storecreditcard():
    """place order with storecredit with card"""
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

@given('update the storecredit from magento')
def store_creditt(driver):
    db= MySQLdb.connect(host="139.162.51.169", user="root", passwd="!qazmlp)5", db="v3_5", port=3306)
    cur = db.cursor()
    updatequery="""UPDATE m_credit_balance SET amount=0 WHERE customer_id=50263"""     
    query = """UPDATE m_credit_balance SET amount =100 WHERE customer_id=50263"""
    cur.execute(updatequery)
    cur.execute(query)
    db.commit()

@given('when a user select location option it redirect to category page')
def a_user_select_location_option_it_redirect_to_category_page(driver):
    locationscreen = pages.AddressPage(driver)
    locationscreen.verify_categorypage()

@given('click category product image chicken it redirect to tcuts product page')
def click_category_product_image_chicken(driver):
    categoryscreen = pages.Homepage(driver)
    categoryscreen.click_categorychicken()
    categoryscreen.verify_tcutspage()


@given("click add button <quantity> from chickencurrycut <product> product")
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
    orderid = paymentpage.get_orderno()
    cache['order_id'] = orderid


@then('verify the order placed in magento <ordertype><paymenttype>')
def verify(cache, ordertype, paymenttype, driver):
    orderid = cache['order_id']
    verify = pages.Verifymagento(driver)
    # verify.sales_ordercard(orderid, ordertype, paymenttype)


@given('select a cash on delivery option')
def select_cash_on_delivery_option(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_cod()


@when('a user click place order button it redirect to continue shopping page')
def a_user_click_place_order_button_it_redirect_to_continue_shopping_page(cache,driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_place_order()
    orderid=paymentpage.get_orderno()
    cache['order_id'] = orderid


    

@given('check store credit applied')
def storecreditt(driver):
    storecreditpage = pages.Storecredit(driver)
    storecreditpage.storecreditapplied()


@given('check cash on delivery option auto selected')
def storecredit(driver):
    storecreditpage = pages.Storecredit(driver)
    storecreditpage.autoselectcod()

