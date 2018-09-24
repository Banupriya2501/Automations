
"""

This module to check signin functionality

"""
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Productpage(lib.BasePage):
    ID_PRODUCT ="search-header-product"
    CSS_PRODUCT_SELECT = ".row > div.col-sm-3"

    def __init__(self, driver):
        super().__init__(driver)


    def select_product(self):
        WebDriverWait(self.driver, 25).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#loading_mask_loader')))
        self.driver.execute_script("window.scrollBy(0, -350);")
        self.driver.find_element_by_css_selector("div.form-buttons > button.scalable.add").click()
        self.driver.find_element_by_id("sales_order_create_search_grid_filter_name").clear()
        self.driver.find_element_by_id("sales_order_create_search_grid_filter_name").send_keys("lolli")
        self.driver.find_element_by_id("sales_order_create_search_grid_filter_name").send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#loading_mask_loader')))

        self.driver.find_element_by_class_name("checkbox").click()
        self.driver.find_element_by_name("qty").send_keys('1')
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#loading_mask_loader')))

        self.driver.find_element_by_xpath(".//*[@id='order-search']/div/div/div[1]").click()