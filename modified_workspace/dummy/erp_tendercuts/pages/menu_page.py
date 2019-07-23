
"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Menupage(lib.BasePage):
    ID_USERNAME = "login"
    ID_PASSWORD = "password"
    CSS_SUBMIT="button.btn.btn-primary"

    def __init__(self, driver):
        super().__init__(driver)


    def humberger_menu(self):
        time.sleep(1)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, 'html/body/header/nav[2]/div[1]/div[1]/a/i')))
        self.driver.find_element_by_xpath('html/body/header/nav[2]/div[1]/div[1]/a/i').click()


    def sales_menu(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sales')))
        self.driver.find_element_by_link_text("Sales").click()

    def purchase_menu(self):
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Purchases')))
        self.driver.find_element_by_link_text("Purchases").click()

    def inventory_menu(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Inventory')))
        self.driver.find_element_by_link_text("Inventory").click()

    def manufacture_menu(self):
        self.driver.find_element_by_xpath(".//*[@id='appDrawerAppPanelBody']/ul/li[6]/a/img").click()

    def invoice_menu(self):
        self.driver.find_element_by_xpath(".//*[@id='appDrawerAppPanelBody']/ul/li[7]/a/img").click()

    def project_menu(self):
        self.driver.find_element_by_xpath(".//*[@id='appDrawerAppPanelBody']/ul/li[8]/a/img").click()

    def attedance_menu(self):
        self.driver.find_element_by_xpath(".//*[@id='appDrawerAppPanelBody']/ul/li[9]/a/img").click()

    def employees_menu(self):
        self.driver.find_element_by_xpath(".//*[@id='appDrawerAppPanelBody']/ul/li[10]/a/img").click()


        