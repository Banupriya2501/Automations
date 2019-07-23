import time
import pytest
from appium import webdriver
from pytest_bdd import given, scenario, then, when
import lib
import pages


@scenario('test_forgetpassword.feature', 'forgetpassword alert')
def test_forgetpassword():
    """check forgetpassword"""
    pass


@given('username')
def username():
    print('')


@when('a user click forgetpassword link and enter username<username>')
def a_user_click_forgetpassword_link(username, driver):
    forgetpsd = pages.ForegetpasswordPage(driver)
    forgetpsd.click_forgetpassword_link()
    forgetpsd.enter_phonenumber(username)
    forgetpsd.click_sendotp()


@then('verify toast message <toastmessage>')
def verify_toast_message(toastmessage, driver):
    loginscreen = pages.SignInPage(driver)
    loginscreen.verify_toast(toastmessage)
