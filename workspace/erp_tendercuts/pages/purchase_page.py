
"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Purchasepage(lib.BasePage):
    ID_USERNAME = "login"
    ID_PASSWORD = "password"
    CSS_SUBMIT="button.btn.btn-primary"

    def __init__(self, driver):
        super().__init__(driver)


    def sub_menu_autoindent(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Auto Indent')))
        self.driver.find_element_by_link_text('Auto Indent').click()

    def projection(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Projections')))
        self.driver.find_element_by_link_text('Projections').click()

    def import_projection(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[1]/div[2]/div[1]/div/button[2]')))
        self.driver.find_element_by_xpath('html/body/div[1]/div/div[1]/div[2]/div[1]/div/button[2]').click()

    def loadfile(self,projectionsheet):  
        time.sleep(0.5)
        # WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//label/input[@type="file"]')))
        self.driver.find_element_by_xpath("//label/input[@type='file']").send_keys(projectionsheet)
           
    def test_import(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '(//button[@type="button"])[7]')))
        self.driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        time.sleep(1)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.XPATH, 'html/body/div[1]/div/div[2]/form/div[2]/div[3]/ul/li/span')))
        msg=self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/form/div[2]/div[3]/ul/li/span")
        assert msg.text == 'Everything seems valid.'

    def import_file(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[1]/div[2]/div[1]/button[2]')))
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[2]/div[1]/button[2]").click()
        time.sleep(1)
        print("****File upload is success for projection******")
        
    def indent(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Indent')))
        self.driver.find_element_by_link_text('Indent').click()

    def loadfile_indent(self,indentsheet):
        # WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//label/input[@type="file"]')))     
        self.driver.find_element_by_xpath("//label/input[@type='file']").send_keys(indentsheet)
         
    def projection_to_done(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[1]/div[1]/div/div/div[2]')))
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[1]/div/div/div[2]").click()

    def indent_date(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[2]/div/div/div/table/thead/tr/th[2]')))
        self.driver.find_element_by_xpath('html/body/div[1]/div/div[2]/div/div/div/table/thead/tr/th[2]').click()   
        time.sleep(0.5)
        self.driver.find_element_by_xpath('html/body/div[1]/div/div[2]/div/div/div/table/thead/tr/th[2]').click()   
        time.sleep(0.5)
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[2]/div/div/div/table/tbody/tr[1]/td[1]/div/input')))
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/table/tbody/tr[1]/td[1]/div/input").click()

    def action(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Action")]')))

        self.driver.find_element_by_xpath('//button[contains(text(),"Action")]').click()   
    
    def generate_indent(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Generate Indent')))
        self.driver.find_element_by_link_text('Generate Indent').click()    

    def getponumber(self,indentdate):
        time.sleep(1)
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//td[2][contains(text(),"+'indentdate'+")]')))

        self.driver.find_element_by_xpath("//td[2][contains(text(),'"+indentdate+"')]").click()   
        
        po_number=self.driver.find_element_by_xpath('//td[contains(text(),"PO")]').text
        return po_number

    #autoindent

    def auto_indent(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Auto Indent PO')))
        self.driver.find_element_by_link_text('Auto Indent PO').click() 

    def pending_record(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[1]/div[1]/div/div/div[2]')))
        self.driver.find_element_by_xpath('html/body/div[1]/div/div[1]/div[1]/div/div/div[2]').click()

    def check_box(self,po_number):
        time.sleep(0.5)
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[2]/div/div/div/table/tbody/tr[1]/td[1]/div/input')))
        self.driver.find_element_by_xpath("//td[2][contains(text(),'"+po_number+"')]").click()

    def conform_order(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Confirm order')))
        self.driver.find_element_by_link_text('Confirm order').click()   
        # time.sleep(0.5)


