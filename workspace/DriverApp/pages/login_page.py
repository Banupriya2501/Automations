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
    CSS_USERNAME = "#phone > input"
    CSS_PASSWORD = "#password > input"
    CSS_EYE = ".type-toggle"
    CSS_SUBMIT="#login-submit"
    CSS_STOREPICKER=".list > ion-template + ion-template + ion-template + ion-template + ion-template > ion-item > div"

    def __init__(self, driver):
        super().__init__(driver)


    def enter_username(self, username):
        # self.driver.implicitly_wait(15)
        time.sleep(6)
        # update=self.driver.find_element_by_css_selector('#ok-button')
        # action = TouchActions(self.driver)
        # action.tap(update).perform()

        # self.driver.implicitly_wait(15)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_USERNAME)))
        self.driver.find_element_by_css_selector(self.CSS_USERNAME).send_keys(username)
        time.sleep(0.5)
        

    def enter_password(self, password):
      
        time.sleep(0.5)
        eye = self.driver.find_element_by_css_selector(self.CSS_EYE)
        eye.click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector(self.CSS_PASSWORD).send_keys(password)
        eye.click()

    def submit(self):
       
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_SUBMIT)))
        
        self.driver.find_element_by_css_selector(self.CSS_SUBMIT).click()


    # def verify(self):
    #     """
    #     Verify it redirect to location page
    #
    #     """
    #     time.sleep(2)
    #     self.driver.implicitly_wait(7)
    #     result=self.driver.find_element_by_css_selector(self.CSS_STOREPICKER).is_displayed()
    #     assert (True == result)
