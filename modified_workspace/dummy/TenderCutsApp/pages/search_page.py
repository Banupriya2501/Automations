"""
this module to verify the search functionality

"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


import lib


class SearchPage(lib.BasePage):
    CSS_SEARCH = "#search-button"
    CSS_SEARCH_ENTER = ".searchbar-input"
    CSS_CLICK_ADD ="ion-row > ion-col + ion-col + ion-col > tcuts-counter > ion-grid > ion-row > ion-col > button"
    CSS_ADD =".listing > tcuts-product >ion-grid#CHK_WHL_SKIN_OFF > ion-row"
    CSS_ARROWBACK ="page-view > ion-header > ion-navbar > button.back-button"
    CSS_LOADER="div >div.loading-spinner >ion-spinner.spinner"
    


    def __init__(self, driver):
        super().__init__(driver)

    def click_search(self):
        """
        click serach button

        """
        time.sleep(5)
        Search = self.driver.find_element_by_css_selector(self.CSS_SEARCH)
        action = TouchActions(self.driver)
        action.tap(Search).perform()

    def enter_chickenproduct(self):
        """
        pass chicken curry cut value to the field

        """
        time.sleep(5)
        self.driver.find_element_by_css_selector(self.CSS_SEARCH_ENTER).click()
        self.driver.find_element_by_css_selector(self.CSS_SEARCH_ENTER).send_keys('chicken curry cut')
        self.driver.press_keycode(61)
        time.sleep(5)

    def click_addbutton(self): 
        """
        click add button
        """
        add=self.driver.find_element_by_css_selector(self.CSS_CLICK_ADD)
        action = TouchActions(self.driver)
        action.tap(add).perform()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.CSS_LOADER)))
        # time.sleep(5)
        # WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_ARROWBACK)))
        # self.driver.find_element_by_css_selector(self.CSS_ARROWBACK).click()



