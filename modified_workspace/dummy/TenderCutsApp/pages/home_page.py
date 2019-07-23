"""
this module to verify homepage
"""
import time

from selenium.webdriver.common.touch_actions import TouchActions

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Homepage(lib.BasePage):
    CSS_CHICKEN_IMAGE = "#cat-4"
    CSS_TITLE = "#category"
    CSS_EMERGENCY="button.got-it-btn"
    CSS_TITLE1 = "#product-title-CHK_BR_BONELESS"

    def __init__(self, driver):
        super().__init__(driver)

    def click_categorychicken(self):
        """
        click chicken image
        """
        try:
            Chickenimage = self.driver.find_element_by_css_selector(self.CSS_CHICKEN_IMAGE)
            if Chickenimage.is_displayed():
                Chickenimage = self.driver.find_element_by_css_selector(self.CSS_CHICKEN_IMAGE)
                action = TouchActions(self.driver)
                action.tap(Chickenimage).perform()
        except:
            self.emergency()

    def verify_tcutspage(self):
        """
        verify title displays in category page
        """
        time.sleep(2)
        self.driver.implicitly_wait(7)
        result = self.driver.find_element_by_css_selector(self.CSS_TITLE).is_displayed()
        assert (True == result)

    def emergency(self):
        try:
            time.sleep(0.1)
            emg=self.driver.find_element_by_css_selector(self.CSS_EMERGENCY)
            if emg.is_displayed():
                self.driver.find_element_by_css_selector(self.CSS_EMERGENCY).click()
                Chickenimage = self.driver.find_element_by_css_selector(self.CSS_CHICKEN_IMAGE)
                action = TouchActions(self.driver)
                action.tap(Chickenimage).perform()
        except:
            self.rate()


    def rate(self):
        try:
            rate=self.driver.find_element_by_css_selector("button.not-now-btn")
            action = TouchActions(self.driver)
            action.tap(rate).perform()
            Chickenimage = self.driver.find_element_by_css_selector(self.CSS_CHICKEN_IMAGE)
            action = TouchActions(self.driver)
            action.tap(Chickenimage).perform()
        except:
            print("")
