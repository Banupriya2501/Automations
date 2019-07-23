import pages
from pytest_bdd import given, scenario, then, when


@scenario('test_signup.feature', 'signup')
def test_signup():
    """verify signup"""
    pass


@given('a signup link')
def a_user_click_signup_link(driver):
    signup = pages.SignupPage(driver)
    signup.click_signup_link()


@when('enter the details <name> ,<email>, <phone>, <password> and <conformpassword>')
def enter_the_details(name, email, phone, password, conformpassword, driver):
    signup = pages.SignupPage(driver)
    signup.enter_signupdetail(name, email, phone, password, conformpassword)


@then('click signup button')
def click_signup_button(driver):
    signup = pages.SignupPage(driver)
    signup.click_signupbutton()


@then('verify it redirect to OTP page')
def verify_it_redirect_to_OTP_page(driver):
    signup = pages.SignupPage(driver)
    signup.verify_otp_page()
