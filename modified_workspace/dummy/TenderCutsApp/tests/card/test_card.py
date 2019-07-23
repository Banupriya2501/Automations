import time
import pytest
from appium import webdriver
from pytest_bdd import given, scenario, then, when
import lib
import pages

# @scenario('test_card.feature', 'payment with added card')
# def test_addedcard():
#     """Order placing via added card"""
#     pass

@pytest.fixture()
def cache():
    return {}


@given('a username <username> and password <password>')
def a_username_and_password(username, password, driver):
    """a username <username> and <password> """
    loginscreen = pages.SignInPage(driver)
    loginscreen.enter_username(username)
    loginscreen.enter_password(password)

@when('when a user click login button it redirect to location page')
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
    tcutproductpage.click_product_add(product)
    tcutproductpage.add_one(quantity)

@then('check proceed option enable')
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
    time.sleep(0.3)
    deliveysummarypage.click_continue()
    deliveysummarypage.verify_paymentpage()

@then('a new added card')
def added_card(driver):
	paymentpage = pages.PaymentPage(driver)
	paymentpage.add_card()

@then ('enter card numnber <card>')
def enter_cardnumber(driver, card):
	paymentpage = pages.PaymentPage(driver)
	paymentpage.card_number(card)

@then('enter mm,yy <mmyy>')
def enter_monthyear(driver, mmyy):
	paymentpage = pages.PaymentPage(driver)
	paymentpage.month_year(mmyy)

@then('select a card and enter cvv number')
def select_card_and_enter_cvv_number(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_card1()    

@then('click on Add New Card')
def new_card(driver):
	paymentpage = pages.PaymentPage(driver)
	paymentpage.save_card()

@then('click on back button in Payment page')
def payment_back(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.pay_back()

@then('click on back button in Delivery Summary')
def delivary_back(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.deli_back()        

@then('click on back button in Cart Summary')
def delivary_back(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.cart_back()

@then('a user click place order button it redirect to bank page')
def bank_page(driver):
    time.sleep(0.5)
    paymentpage = pages.PaymentPage(driver)
    paymentpage.click_place_order()

@then('a user click success button from razor payment')
def click_success_button(cache, driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.card_success()
    orderid = paymentpage.get_orderno()
    cache['order_id'] = orderid

@then('verify the order placed in magento <ordertype> <paymenttype>')
def verify(cache, ordertype, paymenttype, driver):
    orderid = cache['order_id']
    #verify = pages.Verifymagento(driver)
    #verify.sales_ordercard(orderid, ordertype, paymenttype)                

@then('click my accountpage tab')
def my_accountpage(driver):
    address = pages.MyAccountepage(driver)
    address.click_myaccounticon()

@then('click on Manage Payment')
def manage_pay(driver):
    address = pages.MyAccountepage(driver)
    address.mpayment()

@then('click on Delete Button')
def delete_button(driver):
    address = pages.MyAccountepage(driver)
    address.delete_card()

@then('click on Home Icon')
def home_icon(driver):
    address = pages.MyAccountepage(driver)
    address.click_homeicon()

@then('click on continue shopping')
def continue_shopping(driver):
    paymentpage = pages.PaymentPage(driver)
    paymentpage.cshopping()

       
