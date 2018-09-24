
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
    ID_USERNAME = "login"
    ID_PASSWORD = "password"
    CSS_SUBMIT="button.btn.btn-primary"

    def __init__(self, driver):
        super().__init__(driver)


    def enter_logindetails(self,username,password):
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sign in')))
        self.driver.find_element_by_link_text('Sign in').click()
        self.driver.find_element_by_id(self.ID_USERNAME).clear()
        self.driver.find_element_by_id(self.ID_USERNAME).send_keys(username)
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id(self.ID_PASSWORD).send_keys(password)
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_css_selector(self.CSS_SUBMIT).click()

        