import pages
import time
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('test_existing_customer.feature', 'placing order with existing customer')
def test_existing_customer():
    """Existing customer placing order."""
    pass

@scenario('test_new_customer.feature', 'placing order with new customer')
def test_new_customer():
    """New customer placing order."""
    pass

@scenario('test_barcode_customer.feature', 'placing order with barcode and reward points')
def test_barcode_customer():
    """existing customer placing order with barcode scanning."""
    pass


@given('a username and password click submit button')
def a_username_username_and_password_click_submit_button(driver):
    """a username <username> and <password> click submit button."""
    loginpage=pages.Loginpage(driver)
    loginpage.enter_logindetails()

@when('on selection of product')
def product(driver):
    productpage=pages.Productpage(driver)
    productpage.select_product()

@then('enter the existing customer phone number')
def customer(driver):
    customerpage=pages.Customerpage(driver)
    customerpage.select_customer()
    customerpage.checkout()

@then('click payment type')
def payment(driver):
    paymentpage=pages.Paymentpage(driver)
    paymentpage.payment()

@then('check order placed in magento')
def magento(driver):
    print('selection')


@then('enter the new customer phone number')
def new_customer(driver):
    customerpage=pages.Customerpage(driver)
    customerpage.new_customer()
    customerpage.checkout()

@when('on selection of product with barcode')
def barcode(driver):
    productpage=pages.Productpage(driver)
    productpage.barcode()


@then('apply reward points')
def rewardpoints(driver):
    paymentpage=pages.Paymentpage(driver)
    paymentpage.rewardpoints()
    paymentpage.payment()



