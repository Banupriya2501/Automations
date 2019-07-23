from pytest_bdd import given, scenario, then, when
import pages


@scenario('test_ordertab.feature', 'order details')
def test_order_details():
    """order details"""
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


@then("a user select location option")
def a_user_select_location_option(driver):
    locationscreen = pages.AddressPage(driver)
    locationscreen.verify_categorypage()
    
@then('click order tab')
def order(driver):
    orderpage=pages.OrderPage(driver)
    orderpage.click_order_tab()


@then('verify visiblity of live order and past order')
def order(driver):
    orderpage=pages.OrderPage(driver)
    orderpage.check_orders()

@then('click view details button and verify status')
def order(driver):
    orderpage=pages.OrderPage(driver)
    orderpage.click_view_details()
    orderpage.order_status()


@then('click back button')
def order(driver):
    orderpage=pages.OrderPage(driver)
    orderpage.click_back()
