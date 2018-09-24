"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Paymentpage(lib.BasePage):
     
    CSS_CASH = ".payment"
    CSS_PLACEORDER="#checkout_button"
    CSS_REWARDPOINTS=".button btn-cl-cfg-active"
 

    def __init__(self, driver):
        super().__init__(driver)


    def payment(self):
        self.driver.implicitly_wait(55)
        self.driver.find_element_by_css_selector(self.CSS_CASH).click()
        time.sleep(3)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector(self.CSS_PLACEORDER).click()

    def rewardpoints(self):
    	self.driver.implicitly_wait(5)
     #    self.driver.find_element_by_css_selector(self.CSS_REWARDPOINTS).click()