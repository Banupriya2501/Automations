from pytest_bdd import given, scenario, then, when
import pages


@scenario('test_out_service_location.feature', 'out of service')
def test_out_service_location():
    """check out of service alert"""
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
    locationscreen.add_new_address()


@then("a user select location option")
def a_user_select_location_option(driver):
    locationscreen = pages.LocationPage(driver)
    # locationscreen.select_option()


@then('verify toast message <toastmessage>')
def verify_toast_message(toastmessage, driver):
    loginscreen = pages.SignInPage(driver)
    loginscreen.verify_toast(toastmessage)
