"""
this module to verify the search functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import lib
import pages


class OrderPage(lib.BasePage):
    CSS_ORDERTAB = "#tab-t0-1"
    CSS_LIVEORDER = "#tab-t1-0"
    CSS_PASTORDER ="#tab-t1-1"
    CSS_VIEWDETAILS="button#view-button"
    CSS_ORDERDETAILS="ion-row.order-status-bar"
    CSS_BACK="#cancel-button"

    def __init__(self, driver):
        super().__init__(driver)

    def click_order_tab(self):
        """
        click serach button

        """
        
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_ORDERTAB)))
        self.driver.find_element_by_css_selector(self.CSS_ORDERTAB).click()

    def check_orders(self):
        """
        pass chicken curry cut value to the field

        """
       
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_LIVEORDER)))
        result=self.driver.find_element_by_css_selector(self.CSS_LIVEORDER).is_displayed()
        result=self.driver.find_element_by_css_selector(self.CSS_PASTORDER).is_displayed()
        assert result == True


    def click_view_details(self):
        
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_VIEWDETAILS)))
        viewdetails=self.driver.find_element_by_css_selector(self.CSS_VIEWDETAILS)
        action = TouchActions(self.driver)
        action.tap(viewdetails).perform()
    
    def order_status(self):
        
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_ORDERDETAILS)))
        result=self.driver.find_element_by_css_selector(self.CSS_ORDERDETAILS).is_displayed()
        assert result == True

    def click_back(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_BACK)))
        self.driver.find_element_by_css_selector(self.CSS_BACK).click()