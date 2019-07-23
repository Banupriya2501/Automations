import time
import pytest
from appium import webdriver
from pytest_bdd import given, scenario, then, when
import lib
import pages

# @scenario('test_rating.feature', 'previous order rating')
# def test_rating():
#     """rating of previous order"""
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

@then('click on rating star')
def rating(driver):
    ratingpage = pages.Ratingpage(driver)
    ratingpage.click_star()

@then('click on taste button')
def taste(driver):
    ratingpage = pages.Ratingpage(driver)
    ratingpage.click_taste()

@then('click on quality button')
def quality(driver):
    ratingpage = pages.Ratingpage(driver)
    ratingpage.click_quality()

@then('enter the comments')
def comments(driver):
    ratingpage = pages.Ratingpage(driver)
    ratingpage.enter_comments()

@then('click on submit button')
def submit(driver):
    ratingpage = pages.Ratingpage(driver)
    ratingpage.click_submit()

@then('click on Rate button')
def rate(driver):
    ratingpage = pages.Ratingpage(driver)
    ratingpage.click_rate()    