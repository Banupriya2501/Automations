"""

This module to check signin functionality

"""
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Customerpage(lib.BasePage):
     
    CSS_CUSTOMER = ".icon-iconPOS-change-customer"
    CSS_ENTER_CUSTOMER="#search-customer"
    CSS_CLICK_CUSTOMERNAME=".phone-number"
    CSS_CHECKOUT="button.button.checkout.btn-cl-cfg-active"
    CSS_NEW_CUSTOMER_BUTTON="#btn-add-new-customer"
    CSS_NAME=".customer-fname"
    CSS_PHONE="#cust-phoneNumber"
    CSS_SAVE=".btn-save  link-cl-cfg"

    def __init__(self, driver):
        super().__init__(driver)


    def select_customer(self):
        import pdb
        pdb.set_trace()
        self.driver.implicitly_wait(55)
        self.driver.find_element_by_css_selector(self.CSS_CUSTOMER).click()
        time.sleep(3)
        self.driver.find_element_by_css_selector(self.CSS_ENTER_CUSTOMER).send_keys('9710243651')
        self.driver.find_element_by_css_selector(self.CSS_ENTER_CUSTOMER).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_css_selector(self.CSS_CLICK_CUSTOMERNAME).click()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_css_selector(self.CSS_CHECKOUT).click()


    def checkout(self):
     	self.driver.implicitly_wait(15)
        
    def new_customer(self):
    	self.driver.implicitly_wait(55)
        # self.driver.find_element_by_css_selector(self.CSS_NEW_CUSTOMER_BUTTON).click()
        # time.sleep(3)
        # self.driver.find_element_by_css_selector(self.CSS_NAME).send_keys('ptest')
        # self.driver.find_element_by_css_selector(self.CSS_PHONE).send_keys('1234567891')
        # self.driver.implicitly_wait(15)
        # self.driver.find_element_by_css_selector(self.CSS_SAVE).click()
       
