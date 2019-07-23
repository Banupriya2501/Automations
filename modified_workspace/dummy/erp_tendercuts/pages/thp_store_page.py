
"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Thoraipakkampage(lib.BasePage):
    ID_USERNAME = "login"
    ID_PASSWORD = "password"
    CSS_SUBMIT="button.btn.btn-primary"

    def __init__(self, driver):
        super().__init__(driver)


    def switch_to_thoraipakkam(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//a/span[contains(text(),"Administrator")]')))
        self.driver.find_element_by_xpath('//a/span[contains(text(),"Administrator")]').click()
        self.driver.find_element_by_xpath('//a[contains(text(),"Log out")]').click()
        time.sleep(1)
        self.driver.find_element_by_id(self.ID_USERNAME).send_keys('thoraipakkamstore@tendercuts.in')
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id(self.ID_PASSWORD).send_keys('qwerty123')
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_css_selector(self.CSS_SUBMIT).click()

    def purchase_order(self,storedate):
        # WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//th[contains(text(),"22 Sep")]')))
        self.driver.find_element_by_xpath("//th[contains(text(),'"+storedate+"')]").click()

    def click_po(self,po_number):
        # WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//td[contains(text(),"Sea Food")]')))

        self.driver.find_element_by_xpath("//td[contains(text(),'"+po_number+"')]").click()

    def receive_product(self):
        time.sleep(1)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Receive Products")]')))

        self.driver.find_element_by_xpath('//button[contains(text(),"Receive Products")]').click()

    def vendor_bill(self,scannedbill):
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.NAME, 'vendor_reference')))
        self.driver.find_element_by_name('vendor_reference').send_keys('123456')
        time.sleep(0.4)
        self.driver.find_element_by_css_selector("div.o_hidden_input_file.o_hidden > form.o_form_binary_form > input[name=\"ufile\"]").send_keys(scannedbill)
        
    def receive_product_bill(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button//span[contains(text(),"Receive Products")]')))
        self.driver.find_element_by_xpath('//button//span[contains(text(),"Receive Products")]').click()

    def edit(self):
        time.sleep(1)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Edit")]')))
        self.driver.find_element_by_xpath('//button[contains(text(),"Edit")]').click()

    def zero(self):
        time.sleep(0.5)
        # WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]')))
        
        self.driver.find_element_by_xpath('html/body/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]').click()
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.NAME, 'quantity_done')))

        self.driver.find_element_by_name("quantity_done").clear()
        self.driver.find_element_by_name("quantity_done").send_keys("10")
        
    def save(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Save")]')))

        self.driver.find_element_by_xpath('//button[contains(text(),"Save")]').click()

    def validate(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Validate")]')))
        self.driver.find_element_by_xpath('//button[contains(text(),"Validate")]').click()
        WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.LINK_TEXT, 'Loading')))



        