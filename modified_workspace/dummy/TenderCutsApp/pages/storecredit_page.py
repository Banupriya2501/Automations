"""
this module to verify the search functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Storecredit(lib.BasePage):
    CSS_STORECREDIT = "#wallet-display"
    CSS_CODAUTOSELECT = "#payment-mode-radio-0 > div.radio-icon"
    CSS_LOADER="div >div.loading-spinner >ion-spinner.spinner"

   
    def __init__(self, driver):
        super().__init__(driver)

    def storecreditapplied(self):
        """
        click serach button

        """
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.CSS_LOADER)))
        result = self.driver.find_element_by_css_selector(self.CSS_STORECREDIT).is_displayed()
        print(result)
        
    def autoselectcod(self):
        """
        pass chicken curry cut value to the field)

        """      
        time.sleep(5)
        result = self.driver.find_element_by_css_selector(self.CSS_CODAUTOSELECT).is_enabled()
        print(result)
