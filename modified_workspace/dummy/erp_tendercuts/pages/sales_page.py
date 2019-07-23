
"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import lib


class Salespage(lib.BasePage):
    ID_USERNAME = "login"
    ID_PASSWORD = "password"
    CSS_SUBMIT="button.btn.btn-primary"

    def __init__(self, driver):
        super().__init__(driver)


    def click_so(self,so_number):
        time.sleep(1)
        # WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.LINK_TEXT, so_number)))
        self.driver.find_element_by_xpath("//td[2][contains(text(),'"+so_number+"')]").click()

    def confirm_sale(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.XPATH, 'html/body/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/button[7]')))
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/button[7]").click()

    def delivery(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.NAME, 'delivery_count')))
        
        self.driver.find_element_by_name('delivery_count').click()

    def edit(self):
        time.sleep(0.5)
        
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.XPATH, 'html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/button[1]')))
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/button[1]").click()

    def plu_code(self):
        time.sleep(0.5)
        
        plucode=self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[7]").text
        self.driver.find_element_by_name("plu_code").click()
        self.driver.find_element_by_name("plu_code").send_keys(plucode)
        self.driver.find_element_by_name("plu_code").send_keys(Keys.ENTER)
        Salespage.enter_quantity(self)
        Salespage.confirm_batch(self)
        time.sleep(1.5)
        plucode=self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[7]").text
        self.driver.find_element_by_name("plu_code").click()
        self.driver.find_element_by_name("plu_code").send_keys(plucode)
        self.driver.find_element_by_name("plu_code").send_keys(Keys.ENTER)
        Salespage.enter_quantity(self)
        Salespage.confirm_batch(self)


    def enter_quantity(self):
        time.sleep(0.5)
        
        self.driver.find_element_by_xpath("html/body/div[6]/div/div/div[2]/div/div/div/div[3]/div[2]/table/tbody/tr[1]/td[6]").click()
        self.driver.find_element_by_name("consumed_qty").clear()
        self.driver.find_element_by_name("consumed_qty").send_keys("10")


    def confirm_batch(self):
        time.sleep(0.5)
        
        self.driver.find_element_by_name("action_batch_selection").click()

    def put_in_pack(self):
        time.sleep(0.5)
        
        self.driver.find_element_by_name("put_in_pack_name").click()

    def box_number(self):
        time.sleep(0.5)
        
        self.driver.find_element_by_name("pack_name").click()
        self.driver.find_element_by_name("pack_name").send_keys("100")

    def confirm(self):
        time.sleep(0.5)
        
        self.driver.find_element_by_name("action_put_in_pack").click()

    def save(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/button[1]").click()

    def validate(self):
        time.sleep(0.5) 
        self.driver.find_element_by_xpath("//button[contains(text(),'Validate')]").click()

    def switch_purchase_store_login(self):
        time.sleep(10)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//a/span[contains(text(),"Purchase Manager")]')))
        self.driver.find_element_by_xpath('//a/span[contains(text(),"Purchase Manager")]').click()
        self.driver.find_element_by_xpath('//a[contains(text(),"Log out")]').click()
        time.sleep(1)


    