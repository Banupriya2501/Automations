import pages
import time
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('test_expressorder.feature', 'placing express order')
def test_express_order():
    """Existing customer placing order."""
    pass

@scenario('test_schedule_today.feature', 'placing schedule today order')
def test_schedule_today():
    """New customer placing order."""
    pass

@scenario('test_schedule_torow.feature', 'placing schedule torow order')
def test_schedule_torow():
    """existing customer placing order with barcode scanning."""
    pass


@given('a username and password click submit button')
def a_username_username_and_password_click_submit_button(driver):
    """a username <username> and <password> click submit button."""
    loginpage=pages.Loginpage(driver)
    loginpage.enter_logindetails()

@when('user select the customer')
def customer(driver):
    customerpage=pages.Customerpage(driver)
    customerpage.select_customer()

@then('select the store')
def payment(driver):
    storepage=pages.Storepage(driver)
    storepage.select_store()

@then('add product to cart')
def product(driver):
    productpage=pages.Productpage(driver)
    productpage.select_product()


@then('select delivery type and express time slot')
def new_customer(driver):
    paymentpage=pages.Paymentpage(driver)
    paymentpage.payment()
    paymentpage.delivery()

@then('select delivery type and schedule today time slot')
def new_customer(driver):
    paymentpage=pages.Paymentpage(driver)
    paymentpage.payment()
    paymentpage.delivery()
    paymentpage.schedule_today()
    

@then('select delivery type and schedule torow time slot')
def new_customer(driver):
    paymentpage=pages.Paymentpage(driver)
    paymentpage.payment()
    paymentpage.delivery()
    paymentpage.schedule_torow()

@then('place the order')
def submit(driver):
    paymentpage=pages.Paymentpage(driver)
    paymentpage.submit()





