
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
        import pdb
        pdb.set_trace()
        self.driver.implicitly_wait(55)
        self.driver.find_element_by_id(self.ID_PRODUCT).send_keys('chicken curry cut')
        time.sleep(3)
        self.driver.find_element_by_id(self.ID_PRODUCT).send_keys(Keys.ENTER)
        self.driver.find_element_by_css_selector(self.CSS_PRODUCT_SELECT).click()

    def barcode(self):
        self.driver.implicitly_wait(55)
        self.driver.find_element_by_id(self.ID_PRODUCT).send_keys('19301000')
        time.sleep(3)
        