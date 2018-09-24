
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
        self.driver.implicitly_wait(55)
        self.driver.find_element_by_xpath(".//*[@id='username']").send_keys("banutester")
        self.driver.find_element_by_xpath(".//*[@id='login']").send_keys("banu123")
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div/div[5]/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='message-popup-window']/div[1]/a/span").click()
      