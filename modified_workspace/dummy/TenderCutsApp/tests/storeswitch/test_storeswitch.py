from appium import webdriver
from pytest_bdd import given, scenario, then, when
import lib
import pages
import time


@scenario('test_storeswitch.feature', 'store switch from location')
def test_storeswitch():
    """verify the location switched from the address"""
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

@then('when a user select location option it redirect to category page')
def a_user_select_location_option_it_redirect_to_category_page(driver):
    locationscreen = pages.AddressPage(driver)
    locationscreen.verify_categorypage()


@then('click category product image chicken it redirect to tcuts product page')
def click_category_product_image_chicken(driver):
    categoryscreen = pages.Homepage(driver)
    categoryscreen.click_categorychicken()
    categoryscreen.verify_tcutspage()


@then("click add button <quantity> from chickencurrycut <product> product")
def click_add_button_from_chickencurrycut_product(product, quantity, driver):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.click_product_add(product)
    tcutproductpage.add_one(quantity)


@then('check proceed option enable')
def proceed_option_enable(driver):
    tcutproductpage = pages.Categorypage(driver)
    tcutproductpage.verify_proceedbutton()


@then('click proceed button it redirect to cartsummary page')
def click_proceed_button_it_redirect_to_cartsummary_page(driver):
    proceed = pages.CartSummaryPage(driver)
    proceed.click_proceed()


@then('click checkout button it redirect to deliverysummary page')
def click_checkout_button_it_redirect_to_deliverysummary_page(driver):
    cartpage = pages.CartSummaryPage(driver)
    cartpage.click_checkout()
    cartpage.verify_deliverypage()


@then('select time slot and select out side delivery address <product>')
def select_time_slot_and_delivery_address(product, driver):
    deliveysummarypage = pages.DeliverySummaryPage(driver)
    deliveysummarypage.select_timeslot(product)
    deliveysummarypage.out_delivery_region()

@then('check store switch alert')
def store_alert(driver):
    deliveysummarypage = pages.DeliverySummaryPage(driver)
    time.sleep(1)
    deliveysummarypage.closer_to_another_store()

@then('verify it redirect to home page')
def home_page(driver):
    locationscreen = pages.LocationPage(driver)
    # locationscreen.verify_categorypage()


@then('verify the humbermenu location')
def humbermenu(driver):
    categoryscreen = pages.Homepage(driver)
    time.sleep(1)
    categoryscreen.click_categorychicken()
    # categoryscreen.verify_tcutspage()
    humbergerpage=pages.Humbergermenu(driver)
    humbergerpage.menu()
    humbergerpage.get_location_name()


