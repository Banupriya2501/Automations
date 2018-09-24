"""
This is for check location page
"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class LocationPage(lib.BasePage):
    CSS_LOCATION_NAME = ".searchbar-input"
    CSS_LOCATION_OPTION = "#search-option-item-1"
    CSS_CHICKEN_IMAGE = "#cat-4"
    CSS_STORE_SWITCH ="div.alert-button-group > button + button"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_location(self, location):
        """
        pass location name and select option 1
        :param location: this to pass location name
        """
        time.sleep(0.5)
        self.driver.implicitly_wait(20)
        Location = self.driver.find_element_by_css_selector(self.CSS_LOCATION_NAME)
        time.sleep(1)
        Location.send_keys(location)

    def select_option(self):
        """
        select location option
        """
        time.sleep(1)
        self.driver.implicitly_wait(9)
        option = self.driver.find_element_by_css_selector(self.CSS_LOCATION_OPTION)
        action = TouchActions(self.driver)
        action.tap(option).perform()
        
    def verify_categorypage(self):
        """
        verify chicken image display

        """
        WebDriverWait(self.driver, 25).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'ion-spinner.spinner')))
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_css_selector(self.CSS_CHICKEN_IMAGE).is_displayed()
        assert (True == result)


    def switch_store(self):
        """
        verify switch store
        """
        time.sleep(1)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_STORE_SWITCH)))
        self.driver.find_element_by_css_selector(self.CSS_STORE_SWITCH).click()