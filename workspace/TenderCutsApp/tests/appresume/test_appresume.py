import time
import pytest
from appium import webdriver
from pytest_bdd import given, scenario, then, when
import lib
import pages
import MySQLdb
import datetime

@scenario('test_appresume.feature', 'app resume in category page')
def test_appresume_category():
    """outofstock alert in category page"""
    pass

@scenario('test_appresume.feature', 'app resume in cart summary page and checkout')
def test_appresume_cart_summary():
    """outofstock alert in category page"""
    pass

@scenario('test_appresume.feature', 'app resume in cartsummary page')
def test_appresume_cart():
    """outofstock alert in category page"""
    pass

@scenario('test_appresume.feature', 'app resume in delivery page')
def test_appresume_deliverypage():
    """outofstock alert in category page"""
    pass


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


@then('click add button <quantity> from chickencurrycut <product> product')
def click_add_button_from_chickencurrycut_product(driver,product, quantity):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.click_product_add(product)
    tcutproductpage.add_one(quantity)

@then('run app in background')
def app_resume(driver):
	print(" ")
	# driver.background_app(1)

@then('change the staging advance inventory <productid> <qty> <forecastqty>')
def db_connection(driver, productid, qty, forecastqty):
    inventory=pages.Inventory(driver)
    inventory.gramsinventory(productid, qty, forecastqty)

@then('launch app')
def launch(driver):
	driver.background_app(1)

@then('verify the popup displays')
def popup(driver):
    paymentpage = pages.PaymentPage(driver)
    time.sleep(0.5)
    paymentpage.outofstock_pop()

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
    time.sleep(5)

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

@then('when a user click place order button and it redirects to continueshopping page')
def orderplace(cache,driver):
    paymentpage = pages.PaymentPage(driver)
    time.sleep(6)
    paymentpage.click_place_order()
    orderid=paymentpage.get_orderno()

@then('when a user click place order button')
def a_user_click_place_order_button_it_redirect_to_continue_shopping_page(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_place_order()