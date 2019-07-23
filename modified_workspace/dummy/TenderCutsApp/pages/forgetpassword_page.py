""" This module to check signup functionality"""
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import lib


class ForegetpasswordPage(lib.BasePage):
    CSS_FORGETPASSWORD = ".forgot-password > a"
    CSS_PHONENUMBER = "#phone-number > input"
    CSS_SENDOTP= "#submit-OTP"
  

    def __init__(self, driver):
        super().__init__(driver)

    def click_forgetpassword_link(self):
        """
        click forgetpassword link

        """
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.login-to-checkout-btn')))
        time.sleep(1)
        login_to_checkout=self.driver.find_element_by_css_selector("button.login-to-checkout-btn")
        action = TouchActions(self.driver)
        action.tap(login_to_checkout).perform()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.or-img + a')))
        time.sleep(0.5)
        link=self.driver.find_element_by_css_selector(self.CSS_FORGETPASSWORD)
        action = TouchActions(self.driver)
        action.tap(link).perform()
        time.sleep(1)
       
    def enter_phonenumber(self,username):
        """
        pass name ,emailid,phone number , password , confirm password value
        and click signup button

        """
       
        self.driver.implicitly_wait(12)
        buttons =  self.driver.find_elements_by_tag_name("input")
        for element in buttons:
            ActionChains(self.driver).click(element).perform()
        actions = ActionChains(self.driver)
        actions.send_keys('1111111111')
        actions.perform()

    def click_sendotp(self):
        """
        click send otp page
        """
        time.sleep(0.5)
        buttons =  self.driver.find_elements_by_tag_name("button")
        print(len(buttons))
        for i in range(len(buttons)):
            if i == 3:          
                action = TouchActions(self.driver)
                action.tap(buttons[i]).perform()
       
