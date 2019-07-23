from pytest_bdd import given, scenario, then, when
import pages


@scenario('test_managingaddress.feature', 'managing profile')
def test_managingprofile():
    """check managing profile"""
    pass


@scenario('test_managingaddress.feature', 'managing address')
def test_managingaddresses():
    """check managing address"""
    pass


@scenario('test_managingaddress.feature', 'change password')
def test_changepassword():
    """check change password"""
    pass


@scenario('test_managingaddress.feature', 'Refer a friend')
def test_referafriend():
    """check Refer a friend link"""
    pass


@scenario('test_managingaddress.feature', 'manage payment')
def test_managepayment():
    """check manage payment"""
    pass

# @scenario('test_managingaddress.feature', 'Edit and cancel address')
# def test_editcancel():
#     """check edit and cancel address"""
#     pass

# @scenario('test_managingaddress.feature', 'Edit and save address')
# def test_editsave():
#     """check edit and save address"""
#     pass    


@given('a username <username> and password <password>')
def a_username_and_password(username, password, driver):
    """a username <username> and <password> """
    loginscreen = pages.SignInPage(driver)
    loginscreen.enter_username(username)
    loginscreen.enter_password(password)


@given('when a user click login button it redirect to location page')
def a_user_click_login_button(driver):
    loginscreen = pages.SignInPage(driver)
    loginscreen.submit()

@given('enter the location name')
def enter_the_location(driver):
    """enter <location> """
    locationscreen = pages.AddressPage(driver)
    locationscreen.select_existing_address()


@given('when a user select location option it redirect to category page')
def a_user_select_location_option_it_redirect_to_category_page(driver):
    locationscreen = pages.AddressPage(driver)
    locationscreen.verify_categorypage()
    

@given('click my accountpage tab')
def my_accountpage(driver):
    address = pages.MyAccountepage(driver)
    address.click_myaccounticon()


@given('when user click managing address option')
def click_managingaddress(driver):
    address = pages.MyAccountepage(driver)
    address.click_managingaddress()


@when('default address option visible then click defaulf addres and verify toast message')
def click_defaulf_address(driver):
    address = pages.MyAccountepage(driver)
    # address.click_makedefault()


@then('when delete option visible then click delete button')
def click_delete_button(driver):
    address = pages.MyAccountepage(driver)
    address.click_delete()


@then('click add new address button')
def click_add_new_address_button(driver):
    address = pages.MyAccountepage(driver)
    address.click_addnewaddress()


@then('enter new address details and verify toast message')
def enter_new_address(driver):
    address = pages.MyAccountepage(driver)
    address.enter_address()


@then('click homepage')
def click_homepage(driver):
    address = pages.MyAccountepage(driver)
    address.click_homeicon()


@given('when user click managing profile option')
def click_managingprofile(driver):
    address = pages.MyAccountepage(driver)
    address.click_managingprofile()


@when('edit option visible then enter new name')
def name(driver):
    address = pages.MyAccountepage(driver)
    address.click_edit_name()


@then('verify toast message <toastmessage>')
def verify_toast_message(toastmessage, driver):
    loginscreen = pages.SignInPage(driver)
    loginscreen.verify_toast(toastmessage)


@then('when edit option visible for email then edit email address')
def email(driver):
    address = pages.MyAccountepage(driver)
    address.click_edit_email()


@when('edit option visible for password click the option')
def password(driver):
    address = pages.MyAccountepage(driver)
    address.click_edit_password()


@then('enter new password and conform password <passwordd>')
def enter_password(driver, passwordd):
    address = pages.MyAccountepage(driver)
    address.enter_password(passwordd)

@then('when edit option visible then click edit button')
def click_edit_button(driver):
    address = pages.MyAccountepage(driver)
    address.click_edit()

@then('enter the details flatno<flatno>')
def click_flat(driver, flatno):
    address = pages.MyAccountepage(driver)
    address.edit_flat(flatno)

@then('click save button')
def click_save(driver):
    address = pages.MyAccountepage(driver)
    address.save_address()        

@then('click on backward navigation')
def click_back(driver):
    address = pages.MyAccountepage(driver)
    address.back()

@then('click on cancel button')
def click_cancel(driver):
    address = pages.MyAccountepage(driver)
    address.cancel()    

@then('verify the flat<flat>')
def click_flat(driver, flat):
    address = pages.MyAccountepage(driver)
    address.verify_flat(flat)    

@then('click save address button')
def click_confirm(driver):
    address = pages.MyAccountepage(driver)
    address.confirm_address()    


@then('click change password button')
def change_paassword(driver):
    address = pages.MyAccountepage(driver)
    address.click_change_password()


@given('a refer a friend link')
def link(driver):
    address = pages.MyAccountepage(driver)
    address.referafriend_displays()


@when('on cliking link it redirect to invite friend and earn page')
def invite(driver):
    address = pages.MyAccountepage(driver)
    address.referafriend()


@then('verify whats app link displays')
def whatsapp(driver):
    address = pages.MyAccountepage(driver)
    address.whatsapp_displays()


@given('a managepayment link')
def managepayment(driver):
    address = pages.MyAccountepage(driver)
    address.manage_payment()

@then('verify it displays card detail and delete button')
def verify_card(driver):
    address = pages.MyAccountepage(driver)
    address.check_visible_card()

@then('check address row')
def add_row(driver):
    address = pages.MyAccountepage(driver)
    address.address_verify()

@then('click save address button')
def save_add(driver):
    address = pages.MyAccountepage(driver)
    address.map_address()

@then('verify toast msg <toastmsg>')
def toast(driver, toastmsg):
    address = pages.MyAccountepage(driver)
    address.verify_editaddress(toastmsg)


