"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Paymentpage(lib.BasePage):
     
    CSS_CASH = ".payment"
    CSS_PLACEORDER="#checkout_button"
    CSS_REWARDPOINTS=".button btn-cl-cfg-active"
 

    def __init__(self, driver):
        super().__init__(driver)


    def payment(self):
        
        self.driver.find_element_by_xpath(".//*[@id='p_method_cashondelivery']").click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#loading_mask_loader')))
        
     #    self.driver.find_element_by_css_selector(self.CSS_REWARDPOINTS).click()
    def delivery(self):
       
        self.driver.find_element_by_xpath(".//*[@id='s_method_flatrate_flatrate']").click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#loading_mask_loader')))

    def submit(self):
        
        self.driver.find_element_by_xpath(".//*[@title='Submit Order']").click()
       
    def schedule_today(self):
       
        self.driver.find_element_by_xpath(".//*[@id='scheudle']").click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#loading_mask_loader')))

    def schedule_torow(self):
        self.driver.find_element_by_xpath(".//*[@id='scheudle']").click()
        self.driver.find_element_by_xpath(".//*[@id='slotdisplay']/td[2]/select[1]").send_keys('Tomorrow')
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#loading_mask_loader')))
