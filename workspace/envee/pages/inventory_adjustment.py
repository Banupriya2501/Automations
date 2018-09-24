
"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class InventroyAdjustmentpage(lib.BasePage):
    ID_USERNAME = "login"
    ID_PASSWORD = "password"
    CSS_SUBMIT="button.btn.btn-primary"

    def __init__(self, driver):
        super().__init__(driver)


    def inventory_adjustment(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//nav[2]/div/div/a/i").click()
        time.sleep(0.5)
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//img[@alt='Inventory']").click()
        time.sleep(0.5)
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_link_text("Operations").click()
        time.sleep(0.5)

        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//div[@id='odooMenuBarNav']/div/div/ul[6]/li[4]/ul/li[3]/a/span").click()
        time.sleep(0.5)

        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        time.sleep(0.5)

        self.driver.implicitly_wait(15)
        self.driver.find_element_by_name("name").clear()
        time.sleep(0.5)

        self.driver.implicitly_wait(15)
        self.driver.find_element_by_name("name").send_keys("test")
        time.sleep(0.5)

        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("(//button[@type='button'])[9]").click()
        time.sleep(0.5)

        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/button").click()
        time.sleep(0.8)

        self.driver.implicitly_wait(15)
        self.driver.find_element_by_name("action_reset_product_qty").click()
        time.sleep(0.5)

        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/button[2]").click()

        