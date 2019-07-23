"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class SignInPage(lib.BasePage):
    CSS_USERNAME = "#username > input"
    CSS_PASSWORD = "#password > input"
    CSS_LOGINVIAPASSWORD = ".or-img + a"
    CSS_EYE = ".type-toggle"
    CSS_LOCATION_NAME = ".searchbar-input"
    CSS_LOGIN_OTP ="#phone-number > input"
    CSS_SENTOTP ="#submit-OTP"
    CSS_LOADER="div.loading-spinner"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_phone(self, username):
        
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.login-to-checkout-btn')))
        # WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.CSS_LOADER)))
        time.sleep(2)
        login_to_checkout=self.driver.find_element_by_css_selector("button.login-to-checkout-btn")
        action = TouchActions(self.driver)
        action.tap(login_to_checkout).perform()
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.or-img + a')))
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.CSS_LOGIN_OTP).send_keys(username)

    def send_otp(self):
        """
        login via otp

        """
        time.sleep(0.5)
        otp=self.driver.find_element_by_css_selector(self.CSS_SENTOTP )
        action = TouchActions(self.driver)
        action.tap(otp).perform()

    def enter_username(self, username):
        """
        click loginviapassword link and enter username
        :param username:  This is for passing username in the field

        """
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.login-to-checkout-btn')))
        # WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.CSS_LOADER)))
        time.sleep(2)
        login_to_checkout=self.driver.find_element_by_css_selector("button.login-to-checkout-btn")
        action = TouchActions(self.driver)
        action.tap(login_to_checkout).perform()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_LOGINVIAPASSWORD)))
        self.driver.find_element_by_css_selector(self.CSS_LOGINVIAPASSWORD).click()
        self.driver.implicitly_wait(2)
        element = self.driver.find_element_by_css_selector(self.CSS_USERNAME)
        element.send_keys(username)

    def enter_password(self, password):
        """
        click eye icon for hide the keyboard
        and enter password in the field
        :param password: This is for passing password in the field

        """
        eye = self.driver.find_element_by_css_selector(self.CSS_EYE)
        eye.click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(self.CSS_PASSWORD).send_keys(password)
        eye.click()
        self.driver.implicitly_wait(3)

    def submit(self):
        """
        click login button

        """
        self.driver.implicitly_wait(7)
        self.driver.find_element_by_css_selector("#login-submit").click()

    def verify_locationpage(self):
        """
        Verify it redirect to location page

        """
        time.sleep(2)
        self.driver.implicitly_wait(7)
        result = self.driver.find_element_by_css_selector(self.CSS_LOCATION_NAME).is_displayed()
        assert (True == result)

    def verify_toast(self,toastmessage):
        "Alert "
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.toast-message')))
        toast=self.driver.find_element_by_css_selector('.toast-message').text
        assert toast == toastmessage
