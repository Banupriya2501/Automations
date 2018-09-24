from pytest_bdd import given, scenario, then, when
import pages


@scenario('test_humberger.feature', 'humberger menu')
def test_humberger_menu():
    """check humberger menu"""
    pass

# @scenario('test_humberger.feature', 'location change from humbermenu')
# def test_humberger_change_location():
#     """check humberger menu"""
#     pass


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


@then('click humberger menu')
def humbermenu(driver):

    humbergerpage=pages.Humbergermenu(driver)
    humbergerpage.menu()


@then('verify the menu present')
def menu(driver):
    humbergerpage=pages.Humbergermenu(driver)
    humbergerpage.home()
    humbergerpage.location()
    humbergerpage.faq()
    humbergerpage.contactus()
    humbergerpage.referafriend()
    humbergerpage.logout()


@then('click location from humber menu')
def location_humbermenu(driver):
    humbergerpage=pages.Humbergermenu(driver)
    humbergerpage.click_location()

@then('verify it redirect to category page')
def categorypage(driver):
    locationscreen = pages.LocationPage(driver)
    locationscreen.verify_categorypage()

    

@then('enter the location <changelocation> name')
def enter_the_location(changelocation, driver):
    """enter <location> """
    locationscreen = pages.LocationPage(driver)
    locationscreen.enter_location(changelocation)
    locationscreen.select_option()
    locationscreen.switch_store()

@then('verify the location name')
def location_humbermenu(driver):
    humbergerpage=pages.Humbergermenu(driver)
    humbergerpage.get_location_name()
