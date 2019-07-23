
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

    def sub_menu_purchase(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Purchase')))
        self.driver.find_element_by_link_text('Purchase').click()

    def sub_menu_purchaseorder(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Purchase Orders')))
        
        self.driver.find_element_by_link_text('Purchase Orders').click()


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
        # sheetname = "sheet/projection.xlsx"
        self.driver.find_element_by_xpath("//label/input[@type='file']").send_keys(projectionsheet)
           
    def test_import(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '(//button[@type="button"])[7]')))
        self.driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        time.sleep(0.8)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, 'html/body/div[1]/div/div[2]/form/div[2]/div[3]/ul/li/span')))
        msg=self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/form/div[2]/div[3]/ul/li/span")
        assert msg.text == 'Everything seems valid.'

    def import_file(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[1]/div[2]/div[1]/button[2]')))
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[2]/div[1]/button[2]").click()
        # time.sleep(1)
        print("****File upload is success for projection******")
        
    def indent(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Indent')))
        self.driver.find_element_by_link_text('Indent').click()

    def loadfile_indent(self,indentsheet):
        time.sleep(0.5)
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
        WebDriverWait(self.driver, 2).until(EC.invisibility_of_element_located((By.LINK_TEXT, 'Loading')))  

    def getponumber(self,indentdate):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//td[2][contains(text(),"+'indentdate'+")]")))

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
        time.sleep(1)
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[2]/div/div/div/table/tbody/tr[1]/td[1]/div/input')))
        self.driver.find_element_by_xpath("//td[2][contains(text(),'"+po_number+"')]").click()

    def conform_order(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Confirm order')))
        self.driver.find_element_by_link_text('Confirm order').click()   

    def change_vendor(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Edit")]')))
        self.driver.find_element_by_xpath('//button[contains(text(),"Edit")]').click()
        time.sleep(0.3)
        self.driver.find_element_by_xpath("//input[@class='o_input ui-autocomplete-input']").clear()
        self.driver.find_element_by_xpath("//input[@class='o_input ui-autocomplete-input']").send_keys("TenderCuts - Purchase")
        self.driver.find_element_by_xpath('//a[contains(text(),"TenderCuts - Purchase")]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//button[contains(text(),"Save")]').click()

    def get_so(self):
        so_number=self.driver.find_element_by_name('partner_ref').text
        return so_number

    def filter_remove(self):
        time.sleep(0.5)

        self.driver.find_element_by_xpath("//div/div/div/div/div[2]").click()

    def receive_product(self):
        time.sleep(0.5)

        self.driver.find_element_by_xpath("//button[contains(text(),'Receive Products')]").click()

    def vendor_bill(self,scannedbill):
        time.sleep(0.5)

        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.NAME, 'vendor_reference')))
        self.driver.find_element_by_name('vendor_reference').send_keys('123456')
        time.sleep(0.4)
        self.driver.find_element_by_css_selector("div.o_hidden_input_file.o_hidden > form.o_form_binary_form > input[name=\"ufile\"]").send_keys(scannedbill)
        
    def receive_product_bill(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button//span[contains(text(),"Receive Products")]')))
        self.driver.find_element_by_xpath('//button//span[contains(text(),"Receive Products")]').click()

    def scan_package(self):
        time.sleep(0.5)

        self.driver.find_element_by_xpath("//button[contains(text(),'Scan Package')]").click()

    def barcode(self):
        time.sleep(0.5)

        self.driver.find_element_by_name("barcode").send_keys("100")

    def confirm(self):
        time.sleep(0.5)

        self.driver.find_element_by_name("process").click()
        time.sleep(0.5)

