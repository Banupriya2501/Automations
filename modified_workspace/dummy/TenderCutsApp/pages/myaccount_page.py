"""
This module to verify myaccount tab
"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib
import pages


class MyAccountepage(lib.BasePage):
    CSS_MYACCOUNT = "#tab-t0-2"
    CSS_MYACCOUNT1 = "#tab-t1-2"
    CSS_MANAGINGADDRESS = "ion-row#manage-addresses"
    CSS_MAKEDEFAULT = "#make-default"
    CSS_DELETE = "#delete"
    CSS_ADDNEWADDRESS = ".footer > button"
    CSS_FLATNO = "#flat-no > input"
    CSS_STREET = "#street > input"
    CSS_LOCATIONSELECT = ".gps-button"
    CSS_PINCODE = "#pincode > input"
    CSS_ADDADDRESS = "#add-new-address-submit"
    CSS_HOMEICON = "#tab-t0-0"
    CSS_HOMEICON1 = "#tab-t2-0"
    CSS_MANAGINGPROFILE = "ion-row#manage-profile"
    CSS_EDITOPTION="ion-icon.edit-icon"
    CSS_EDITOPTIONEMAIL=".userProfile > ion-row + ion-row + ion-row + ion-row + ion-row > ion-col + ion-col + ion-col + ion-col >ion-icon.edit-icon"
    CSS_EDITEMAIL="ion-input#emailID > input"
    CSS_EDITNAME="ion-input#userName > input"
    CSS_SAVENAME="ion-col > ion-icon.check-icon"
    CSS_EYE = ".type-toggle"
    CSS_EDITOPTIONPASSWORD="ion-col > ion-icon.edit-pwd"
    CSS_PASSWORD="ion-input#newPass > input"
    CSS_CONFORM_PASSWORD="ion-input#confirmPass > input"
    CSS_CHANGEPASSWORD ="button.new-submit"
    CSS_REFERAFRIENDLINK= "ion-row#refer-earn > ion-col +ion-col + ion-col > ion-icon.arrow"
    CSS_WHATSAPP="div.bottom-part > div.sub-title"
    CSS_MANAGE_PAYMENTLINK="ion-row#manage-payment > ion-col +ion-col + ion-col > ion-icon.arrow"
    CSS_GET_CARDDETAIL="div.act_no"
    CSS_DELETEBUTTON="button > span"
    CSS_EDIT="#edit > span"
    CSS_SAVE="#add-new-address-submit"
    CSS_BACK="body > ion-app > page-map > ion-header > ion-navbar > button"
    CSS_CANCEL="#back-button"
    CSS_MANAGEPAYMENT = "#manage-payment > ion-col:nth-child(3) > ion-icon"
    CSS_DELETECARD = "#cards > ion-template > ion-template > ion-row > ion-col:nth-child(2) > button"
    CSS_DELETECARD_CONFIRMATION = "body > ion-app > ion-alert > div > div.alert-button-group > button:nth-child(2)"
    CSS_ADDRESSROW = "#address-0"
    CSS_SAVEADDRESS = "#save-address-button"

    


    def __init__(self, driver):
        super().__init__(driver)

    def click_myaccounticon(self):
        """
        click myaccount tab

        """
        time.sleep(0.5)
        try:
            myaccount = self.driver.find_element_by_css_selector(self.CSS_MYACCOUNT)
            myaccount.click()
            time.sleep(0.5)
        except:
            myaccount = self.driver.find_element_by_css_selector(self.CSS_MYACCOUNT1)
            myaccount.click()
            time.sleep(0.5)

    def click_managingaddress(self):
        """
        click managing address option
        """
        m = self.driver.find_element_by_css_selector(self.CSS_MANAGINGADDRESS)
        action = TouchActions(self.driver)
        action.tap(m).perform()
        time.sleep(0.5)
        # self.driver.implicitly_wait(5)

    def click_makedefault(self):
        """
        click makedefault link if visible
        """
        try:
            Result = self.driver.find_element_by_css_selector(self.CSS_MAKEDEFAULT).is_displayed()
            if Result == True:
                Default = self.driver.find_element_by_css_selector(self.CSS_MAKEDEFAULT)
                action = TouchActions(self.driver)
                action.tap(Default).perform()
                time.sleep(0.5)
                WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.toast-message')))
                toast=self.driver.find_element_by_css_selector('.toast-message').text
                assert toast == "Default Address Set"
            else:
                print('Not visible of Make Default')
        finally:
            print()
        time.sleep(0.8)

    def click_delete(self):
        """
        click delete link if visible

        """
        Result = self.driver.find_element_by_css_selector(self.CSS_DELETE).is_displayed()
        if Result == True:
            delete = self.driver.find_element_by_css_selector(self.CSS_DELETE)
            action = TouchActions(self.driver)
            action.tap(delete).perform()
        else:
            print('Not visible of Make Default')
        time.sleep(0.2)

    def click_addnewaddress(self):
        """
        click add new address  button
        """
        AddAddress = self.driver.find_element_by_css_selector(self.CSS_ADDNEWADDRESS)
        action = TouchActions(self.driver)
        action.tap(AddAddress).perform()
        time.sleep(0.2)

    def enter_address(self):
        """
        pass  flatno,street,location and pincode value
        """
        self.driver.find_element_by_css_selector(self.CSS_FLATNO).send_keys("11111")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector(self.CSS_STREET).send_keys("11111")
        self.driver.press_keycode(61)
        self.driver.implicitly_wait(5)
        time.sleep(1)
        select = self.driver.find_element_by_css_selector(self.CSS_LOCATIONSELECT)
        action = TouchActions(self.driver)
        action.tap(select).perform()
        self.driver.implicitly_wait(5)
        time.sleep(3)
        loc = pages.LocationPage(self.driver)
        loc.enter_location(location="thorai")
        loc.select_option()
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector(self.CSS_PINCODE).send_keys("602024")
        self.driver.press_keycode(61)
        self.driver.implicitly_wait(5)
        time.sleep(1)
        select = self.driver.find_element_by_css_selector(self.CSS_ADDADDRESS)
        action = TouchActions(self.driver)
        action.tap(select).perform()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.toast-message')))
        toast=self.driver.find_element_by_css_selector('.toast-message').text
        assert toast == "Address Added"

    def click_homeicon(self):
        """
        click home icon
        """
        time.sleep(7)
        try:
            myhome = self.driver.find_element_by_css_selector(self.CSS_HOMEICON)
            myhome.click()
        except:
            myhome = self.driver.find_element_by_css_selector(self.CSS_HOMEICON1)
            myhome.click()

    def click_managingprofile(self):
        """
        click managing profile option
        """
        m = self.driver.find_element_by_css_selector(self.CSS_MANAGINGPROFILE)
        action = TouchActions(self.driver)
        action.tap(m).perform()
        time.sleep(0.2)
        # self.driver.implicitly_wait(5)

    def click_edit_name(self):
        """
        to edit the name
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_EDITOPTION)))
        edit=self.driver.find_element_by_css_selector(self.CSS_EDITOPTION)
        action = TouchActions(self.driver)
        action.tap(edit).perform()
        self.driver.find_element_by_css_selector(self.CSS_EDITNAME).send_keys('B')
        tick=self.driver.find_element_by_css_selector(self.CSS_SAVENAME)
        action = TouchActions(self.driver)
        action.tap(tick).perform()
    
    def click_edit_email(self):
        """
        to edit email address
        """

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_EDITOPTIONEMAIL)))
        edit=self.driver.find_element_by_css_selector(self.CSS_EDITOPTIONEMAIL)
        action = TouchActions(self.driver)
        action.tap(edit).perform()
        self.driver.find_element_by_css_selector(self.CSS_EDITEMAIL).send_keys('c')
        tick=self.driver.find_element_by_css_selector(self.CSS_SAVENAME)
        action = TouchActions(self.driver)
        action.tap(tick).perform()

    def click_edit_password(self):
        """
        to edit password
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_EDITOPTIONPASSWORD)))
        edit=self.driver.find_element_by_css_selector(self.CSS_EDITOPTIONPASSWORD)
        action = TouchActions(self.driver)
        action.tap(edit).perform()
    
    def enter_password(self,password):
        """
        enter password
        """
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_PASSWORD)))
        self.driver.find_element_by_css_selector(self.CSS_PASSWORD).send_keys(password)
        self.driver.find_element_by_css_selector(self.CSS_CONFORM_PASSWORD).send_keys(password)
        self.driver.find_element_by_css_selector(self.CSS_EYE).click()
       

    def click_change_password(self):
        """
        click change password button
        """
        time.sleep(0.8)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_CHANGEPASSWORD)))
        self.driver.find_element_by_css_selector(self.CSS_CHANGEPASSWORD).click()

    def referafriend_displays(self):
        """
        check refer a friend displays
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_REFERAFRIENDLINK)))
        self.driver.find_element_by_css_selector(self.CSS_REFERAFRIENDLINK).is_displayed()


    def referafriend(self):
        """
        check refer a friend link
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_REFERAFRIENDLINK)))
        referafriendlink=self.driver.find_element_by_css_selector(self.CSS_REFERAFRIENDLINK)
        action = TouchActions(self.driver)
        action.tap(referafriendlink).perform()

    def whatsapp_displays(self):
        """
        check whatapp displays
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_WHATSAPP)))
        self.driver.find_element_by_css_selector(self.CSS_WHATSAPP).is_displayed()
     
    def manage_payment(self):
        """
        check manage payment and visiblity of card
        """
        payment=self.driver.find_element_by_css_selector(self.CSS_MANAGE_PAYMENTLINK)
        action = TouchActions(self.driver)
        action.tap(payment).perform()
     

    def check_visible_card(self):
        """
        check card number displays
        """
        Result=self.driver.find_element_by_css_selector(self.CSS_GET_CARDDETAIL).is_displayed()
        assert Result == True

    def click_edit(self):
        self.driver.find_element_by_css_selector(self.CSS_EDIT).click()

    def edit_flat(self,flatno):
        time.sleep(5)
        self.driver.find_element_by_css_selector(self.CSS_FLATNO).send_keys(flatno)

    def save_address(self):
        time.sleep(5)
        self.driver.find_element_by_css_selector(self.CSS_SAVE).click()
        time.sleep(5)

    def back(self):
        time.sleep(5)
        self.driver.find_element_by_css_selector(self.CSS_BACK).click()
        time.sleep(10)

    def cancel(self):
        time.sleep(5)
        self.driver.find_element_by_css_selector(self.CSS_CANCEL).click()
        time.sleep(10)

    def mpayment(self):
        time.sleep(5)
        self.driver.find_element_by_css_selector(self.CSS_MANAGEPAYMENT).click()

    def delete_card(self):
        time.sleep(5)
        self.driver.find_element_by_css_selector(self.CSS_DELETECARD).click()
        time.sleep(8)
        self.driver.find_element_by_css_selector(self.CSS_DELETECARD_CONFIRMATION).click()

    def map_address(self):
        time.sleep(5)
        self.driver.find_element_by_css_selector(self.CSS_SAVEADDRESS).click()
        time.sleep(3)

    def verify_editaddress(self, toastmsg):
        "Alert"
        toast=self.driver.find_element_by_css_selector('.toast-message').text
        assert toast == toastmsg
        
    def address_verify(self):
        time.sleep(5)
        result=self.driver.find_element_by_css_selector(self.CSS_ADDRESSROW).is_displayed()
        if result == True:
            print("Address is there")
        else:
            print("Address is not there")    



