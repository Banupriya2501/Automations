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
        
        self.driver.implicitly_wait(55)
        self.driver.find_element_by_xpath(".//*[@id='sales_order_create_customer_grid_filter_entity_id']").send_keys('38950')
        self.driver.find_element_by_xpath(".//*[@id='sales_order_create_customer_grid_filter_entity_id']").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='sales_order_create_customer_grid_table']/tbody/tr[1]/td[1]").click()
         




       