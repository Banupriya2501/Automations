
"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Pointofsalepage(lib.BasePage):
    ID_USERNAME = "login"
    ID_PASSWORD = "password"
    CSS_SUBMIT="button.btn.btn-primary"

    def __init__(self, driver):
        super().__init__(driver)


    def humberger_menu(self):
        import pdb
        pdb.set_trace()
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//nav[2]/div/div/a/i')))
        self.driver.find_element_by_xpath("//nav[2]/div/div/a/i").click()

    def pos_app(self):
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//img[@alt="Point of Sale"]')))
        self.driver.find_element_by_xpath("//img[@alt='Point of Sale']").click()

    def new_session(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '(//button[@type="button"])[17]')))

        self.driver.find_element_by_xpath("(//button[@type='button'])[17]").click()

    def open_session(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div/div/div/div/div/div/button')))

        self.driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/button").click()

    def continue_selling(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div/div/div/div/div/div/button[2]')))

        self.driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/button[2]").click()


    def product_selection(self):
        import pdb
        pdb.set_trace()
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.product-name')))

        self.driver.find_element_by_css_selector("div.product-name").click()

    def payment(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button.pay')))

        self.driver.find_element_by_css_selector("button.button.pay").click()

    def payment_selection(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.button.paymentmethod')))

        self.driver.find_element_by_css_selector("div.button.paymentmethod").click()

    def number_pad(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section.payment-numpad > div.numpad > button.input-button.number-char')))

        self.driver.find_element_by_css_selector("section.payment-numpad > div.numpad > button.input-button.number-char").click()
        self.driver.find_element_by_xpath("//section[2]/div/button[14]").click()
        self.driver.find_element_by_xpath("//section[2]/div/button[14]").click()

    def validate(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//div[5]/div/div/span[2]')))

        self.driver.find_element_by_xpath("//div[5]/div/div/span[2]").click()

    def close(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div[2]/div/div[1]/div[2]/div[3]')))

        self.driver.find_element_by_xpath("html/body/div[1]/div[2]/div/div[1]/div[2]/div[3]").click()

    def confirm(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.header-button.confirm')))

        self.driver.find_element_by_css_selector("div.header-button.confirm").click()

    def close_adayar(self):
        import pdb
        pdb.set_trace()
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '(//button[@type="button"])[18]')))

        self.driver.find_element_by_xpath("(//button[@type='button'])[18]").click()

    def end_of_session(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//div/div/button[3]')))

        self.driver.find_element_by_xpath("//div/div/button[3]").click()

    def validate_close(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[5]')))

        self.driver.find_element_by_xpath("//button[5]").click()

    def order_menu(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '(//a[contains(text(),"Orders")])[2]')))

        self.driver.find_element_by_xpath("(//a[contains(text(),'Orders')])[2]").click()

    def order_option(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="odooMenuBarNav"]/div/div/ul[4]/li[4]/ul/li/a/span')))

        self.driver.find_element_by_xpath("//div[@id='odooMenuBarNav']/div/div/ul[4]/li[4]/ul/li/a/span").click()