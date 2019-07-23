""" This module to check signup functionality"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class SignupPage(lib.BasePage):
    CSS_SIGNUP = "#sign-up"
    CSS_NAME = "#name > input"
    CSS_EMAIL = "#email > input"
    CSS_PHONE = "#phone > input"
    CSS_PASSWORD = "#password > input"
    CSS_CONFORMPASSWORD = "#confirm > input"
    CSS_SIGNUPBUTTON = "#submit-signup"
    CSS_OTPPAGE = "#otp"

    def __init__(self, driver):
        super().__init__(driver)

    def click_signup_link(self):
        """
        click signup link

        """
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.login-to-checkout-btn')))
        time.sleep(3)
        login_to_checkout=self.driver.find_element_by_css_selector("button.login-to-checkout-btn")
        action = TouchActions(self.driver)
        action.tap(login_to_checkout).perform()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.or-img + a')))
        option = self.driver.find_element_by_css_selector(self.CSS_SIGNUP)
        action = TouchActions(self.driver)
        action.tap(option).perform()
        time.sleep(1)

    def enter_signupdetail(self,name,email,phone,password,conformpassword):
        """
        pass name ,emailid,phone number , password , confirm password value
        and click signup button

        """
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_css_selector(self.CSS_NAME).send_keys(name)
        self.driver.press_keycode(61)
        self.driver.find_element_by_css_selector(self.CSS_EMAIL).send_keys(email)
        self.driver.press_keycode(61)
        self.driver.find_element_by_css_selector(self.CSS_PHONE).send_keys(phone)
        self.driver.press_keycode(61)
        self.driver.find_element_by_css_selector(self.CSS_PASSWORD).send_keys(password)
        self.driver.press_keycode(61)
        self.driver.find_element_by_css_selector(self.CSS_CONFORMPASSWORD).send_keys(conformpassword)
        self.driver.press_keycode(61)
        time.sleep(2)

    def click_signupbutton(self):
        time.sleep(2)
        self.driver.find_element_by_css_selector(self.CSS_SIGNUPBUTTON).click()

    def verify_otp_page(self):
        """
        verify it redirect to Otp verification page
        and close the app

        """
        time.sleep(2)
        self.driver.implicitly_wait(10)
        result = self.driver.find_element_by_css_selector(self.CSS_OTPPAGE).is_displayed()
        assert (True == result)