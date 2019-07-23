from pytest_bdd import given, scenario, then, when
import pages

@scenario('test_geohash.feature', 'geohash fails')
def test_geohash_fails():
    """check add address to home page"""
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

@then('deny the location and verify the alert on map and add address')
def deny(driver):
    locationscreen = pages.AddressPage(driver)
    locationscreen.deny_location()

@then('verify toast message <toastmessage>')
def verify_toast_message(toastmessage, driver):
    loginscreen = pages.SignInPage(driver)
    loginscreen.verify_toast(toastmessage)