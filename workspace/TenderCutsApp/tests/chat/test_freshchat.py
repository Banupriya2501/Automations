import pages
from pytest_bdd import given, scenario, then, when
import pytest


@scenario('test_freshchat.feature', 'fresh chat')
def test_freshchat():
    """fresh chat"""
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
    


@then('when a user enter the location name')
def enter_the_location(driver):
    """enter <location> """
    locationscreen = pages.AddressPage(driver)
    locationscreen.select_existing_address()


@then('a user select location option it redirect to category page')
def a_user_select_location_option_it_redirect_to_category_page(driver):
    locationscreen = pages.AddressPage(driver)
    locationscreen.verify_categorypage()


@then('a user click chat tab it redirect to chat page')
def a_chat_msg_click_on_chat_option(driver):
    chat = pages.Chatpage(driver)
    chat.click_chatoption()


@then('enter a msg and click send msg option')
def click_sendmessage_text(driver):
    chat = pages.Chatpage(driver)
    chat.switchcontext()
    chat.sendmsg()


@then('click Narrow back arrow')
def Narrow_back(driver):
    chat = pages.Chatpage(driver)
    chat.narrow()
    chat.switchtowebview()
    chat.clickhome()
