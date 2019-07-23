import time
import pytest
from appium import webdriver
from pytest_bdd import given, scenario, then, when
import lib
import pages
import MySQLdb
import datetime

@pytest.fixture()
def cache():
    return {}

@scenario('test_outofstock.feature', 'outofstock tcuts')
def test_outofstock_tcuts():
    """outofstock tcuts"""
    pass

@scenario('test_outofstock.feature', 'outofstock cartpage')
def test_outofstockalert_cartpage():
    """outofstock cartpage"""
    pass

@scenario('test_outofstock.feature', 'outofstock payment page')
def test_outofstock_paymentpage():
    """outofstock payment page"""
    pass

@scenario('test_outofstock.feature', 'outofstock and place order')
def test_outofstock_placeorder():
    """outofstock and place order"""
    pass


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
    

@when('click category product image chicken it redirect to tcuts product page')
def click_category_product_image_chicken(driver):
    categoryscreen = pages.Homepage(driver)
    categoryscreen.click_categorychicken()
    categoryscreen.verify_tcutspage()


@then('click add button <quantity> from chickencurrycut <product> product')
def click_add_button_from_chickencurrycut_product(driver,product, quantity):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.click_product_add(product)
    tcutproductpage.add_one(quantity)

@then('check out of stock alert displays')
def outofstock(driver):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.verify_outofstockalert()

@given('change the staging advance inventory <productid> <qty> <forecastqty>')
def db_connection(driver, productid, qty, forecastqty):
    inventory=pages.Inventory(driver)
    inventory.gramsinventory(productid, qty, forecastqty)


@then('click add button from chickencurrycut <product> product')
def click_add_button_from_chickencurrycut_product(product, driver):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.click_product_add(product)


@then('check proceed option enable')
def proceed_option_enable(driver):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.verify_proceedbutton()


@then('click proceed button it redirect to cartsummary page')
def click_proceed_button_it_redirect_to_cartsummary_page(driver):
    proceed = pages.CartSummaryPage(driver)
    proceed.click_proceed()


@then('increase quantityo in cart page <quantity>')
def increase_quantity_cart(quantity, driver):
    tcutproductpage = pages.CartSummaryPage(driver)
    tcutproductpage.cart_product_add(quantity)
    time.sleep(4)


@then("click add button <quantity> from chickencurrycut <product> product")
def click_add_button_from_chickencurrycut_product(product, quantity, driver):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.click_product_add(product)
    tcutproductpage.add_one(quantity)


@when('proceed option enable')
def proceed_option_enable(driver):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.verify_proceedbutton()


@then('click proceed button it redirect to cartsummary page')
def click_proceed_button_it_redirect_to_cartsummary_page(driver):
    proceed = pages.CartSummaryPage(driver)
    proceed.click_proceed()


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

@then('select a cash on delivery option')
def select_cash_on_delivery_option(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_cod()


@then('when a user click place order button')
def a_user_click_place_order_button_it_redirect_to_continue_shopping_page(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_place_order()


@then('verify the popup displays')
def popup(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.outofstock_pop()


@then('when a user click place order button and it redirects to continueshopping page')
def orderplace(cache,driver):
    paymentpage = pages.PaymentPage(driver)
    time.sleep(6)
    paymentpage.click_place_order()
    orderid=paymentpage.get_orderno()
    cache['order_id']=orderid


@then('verify the order placed in magento <ordertype> <paymenttype>')
def verify(cache, ordertype, paymenttype, driver):
    orderid = cache['order_id']
    # verify = pages.Verifymagento(driver)
    # verify.sales_ordercard(orderid, ordertype, paymenttype)


@then('check it redirect to home page')
def home(driver):
    categoryscreen = pages.Homepage(driver)
    # categoryscreen.verify_tcutspage()

@then('change the staging grams inventory <productid> <qty> <forecastqty>')
def dbconnection(driver, productid, qty, forecastqty):
    inventory=pages.Inventory(driver)
    inventory.gramsinventory(productid, qty, forecastqty)

@when('click add button <quantity> from chickencurrycut<product> product')
def click_add_button_from_chickencurrycut_product(product, quantity, driver):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.click_product_add(product)
    tcutproductpage.add_one(quantity)

@given('click category product image chicken it redirect to tcutsproduct page')
def click_category_product_image_chicken(driver):
    categoryscreen = pages.Homepage(driver)
    categoryscreen.click_categorychicken()
    categoryscreen.verify_tcutspage()

@given('click add button<quantity> from chickencurrycut <product> product')
def click_add_button_from_chickencurrycut_product(product, quantity, driver):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.click_product_add(product)
    tcutproductpage.add_one(quantity)

@then('add inventory <productid> <updateqty> <forecastqty>')
def dbconnection(driver, productid, updateqty, forecastqty):
    inventory=pages.Inventory(driver)
    inventory.gramsinventory(productid, updateqty, forecastqty)