"""
this module to verify the search functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions

import lib


class Storecredit(lib.BasePage):
    CSS_STORECREDIT = "#wallet-display"
    CSS_CODAUTOSELECT = "#payment-mode-radio-0 > div.radio-icon"
   
    def __init__(self, driver):
        super().__init__(driver)

    def storecreditapplied(self):
        """
        click serach button

        """
        time.sleep(15)
        result = self.driver.find_element_by_css_selector(self.CSS_STORECREDIT).is_displayed()
        print(result)
        
    def autoselectcod(self):
        """
        pass chicken curry cut value to the field)

        """      
        time.sleep(5)
        result = self.driver.find_element_by_css_selector(self.CSS_CODAUTOSELECT).is_enabled()
        print(result)
