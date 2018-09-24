
"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Inventorypage(lib.BasePage):
    ID_USERNAME = "login"
    ID_PASSWORD = "password"
    CSS_SUBMIT="button.btn.btn-primary"

    def __init__(self, driver):
        super().__init__(driver)


    def humbergermenu(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//nav[2]/div/div/a/i')))
        self.driver.find_element_by_xpath("//nav[2]/div/div/a/i").click()
      
    def inventory(self):     
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//img[@alt="Inventory"]')))
        self.driver.find_element_by_xpath("//img[@alt='Inventory']").click()
      
    def report(self):
        time.sleep(0.4)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '(//a[contains(text(),"Reporting")])[3]')))
        self.driver.find_element_by_xpath("(//a[contains(text(),'Reporting')])[3]").click()
    
    def inventorymenu(self): 
        time.sleep(0.4)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="odooMenuBarNav"]/div/div/ul[6]/li[7]/ul/li/a/span')))
        self.driver.find_element_by_xpath("//div[@id='odooMenuBarNav']/div/div/ul[6]/li[7]/ul/li/a/span").click()
        
    def currentdate(self):
        time.sleep(0.4)
        
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.NAME, 'open_table')))

        self.driver.find_element_by_name("open_table").click()

    def close(self):     
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//div/div[2]/div[2]')))
        time.sleep(0.4)

        self.driver.find_element_by_xpath("//div/div[2]/div[2]").click()  
        self.driver.find_element_by_xpath("//div/div/div/div/div[2]").click() 
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[1]/div/span").click()
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[3]/div[1]/div[2]/button").click()
 
    def location(self):  
        time.sleep(0.4)
        
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[1]/div[3]/div[1]/div[2]/ul/li[1]/a')))
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[3]/div[1]/div[2]/ul/li[1]/a").click()
        
    def whstock(self):
        time.sleep(0.4)
     
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//tr//th[text()[contains(.,"WH/Stock")]]')))
        self.driver.find_element_by_xpath("//tr//th[text()[contains(.,'WH/Stock')]]").click()
        
    def quantity_verification(self):
        time.sleep(0.4)
        
        self.driver.implicitly_wait(15)
        # product_id = ["102","103","104","105","106","107","108","109","301","570"]
        # quantity=["5.00","10.00","15.00","20.00","25.00","30.00","35.00","40.00","45.00","50.00"]
        product_id=["1008"]
        quantity=["5.00"]
        for i in range(0,1):
            WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//tr//td[text()[contains(.,'+ str(product_id[i]) +')]]')))
            self.driver.find_element_by_xpath("//tr//td[text()[contains(.,"+ str(product_id[i]) +")]]").click()
            self.driver.implicitly_wait(15)
            WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//span[@name="quantity"]')))
            qty=self.driver.find_element_by_xpath("//span[@name='quantity']").text   
            assert (quantity[i] == qty)         
            WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[1]/ol/li[2]/a')))
            self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ol/li[2]/a").click()#