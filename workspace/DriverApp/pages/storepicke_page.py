"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import lib



class Storepickerpage(lib.BasePage):

    CSS_STOREPICKER=".list > ion-template + ion-template + ion-template + ion-template + ion-template > ion-item > div"
    CSS_ALERT=".alert-button-group > button + button"

    def __init__(self, driver):
        super().__init__(driver)

    def click_store(self):
        time.sleep(2)
        self.driver.switch_to.context('NATIVE_APP')
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Allow")').click()
        self.driver.switch_to.context('WEBVIEW_com.tendercuts.driver')
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_STOREPICKER)))
        self.driver.implicitly_wait(7)
        self.driver.find_element_by_css_selector(self.CSS_STOREPICKER).click()
        time.sleep(4)
        self.driver.find_element_by_css_selector(self.CSS_ALERT).click()

    def verify(self):
        """
        Verify it redirect to location page

        """
        time.sleep(2)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_STOREPICKER)))
        self.driver.implicitly_wait(7)
        self.driver.find_element_by_css_selector(self.CSS_STOREPICKER).click()
