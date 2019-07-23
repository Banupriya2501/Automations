from pytest_bdd import given, scenario, then, when
import pages


@scenario('test_invalid_login.feature', 'invalid password alert')
def test_invalid_login():
    """check alert for invalid login via password"""
    pass


@scenario('test_invalid_login_otp.feature', 'invalid login otp')
def test_invalid_login_otp():
    """check alert for invalid otp login"""
    pass


@scenario('test_login_otp.feature', 'valid login otp')
def test_login_otp():
    """check valid login redirect to otp page"""
    pass


@given('a username <username> and password <password>')
def a_username_and_password(username, password, driver):
    """a username <username> and <password> """
    loginscreen = pages.SignInPage(driver)
    loginscreen.enter_username(username)
    loginscreen.enter_password(password)


@when('a user click login button')
def a_user_click_login_button(driver):
    loginscreen = pages.SignInPage(driver)
    loginscreen.submit()


@then('verify toast message <toastmessage>')
def verify_toast_message(toastmessage, driver):
    loginscreen = pages.SignInPage(driver)
    loginscreen.verify_toast(toastmessage)


@given('a username <username>')
def a_username(username, driver):
    loginscreen = pages.SignInPage(driver)
    loginscreen.enter_phone(username)


@when('a user click send otp')
def a_user_click_send_otp(driver):
    loginscreen = pages.SignInPage(driver)
    loginscreen.send_otp()


@then('verify it redirect to OTP page')
def verify_it_redirect_to_OTP_page(driver):
    signup = pages.SignupPage(driver)
    signup.verify_otp_page()
