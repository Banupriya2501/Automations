
"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Loginpage(lib.BasePage):
    ID_DROPDOWN ="select_website"
    ID_USERNAME = "username"
    ID_PASSWORD = "pwd"
    CSS_SUBMIT=".form-group > button"

    def __init__(self, driver):
        super().__init__(driver)


    def enter_logindetails(self):
        import pdb
        pdb.set_trace()
        self.driver.implicitly_wait(55)
        el = self.driver.find_element_by_id('select_website')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'pos_adayar':
                option.click() # select() in earlier versions of webdriver
                break
        time.sleep(3)
        # self.driver.find_element_by_id(self.ID_USERNAME).clear()
       # // self.driver.find_element_by_id(self.ID_USERNAME).send_keys('madhu')
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id(self.ID_PASSWORD).send_keys('madhu123')
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id(self.ID_USERNAME).send_keys('madhu')
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_css_selector(self.CSS_SUBMIT).click()
        time.sleep(10)
        