
"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Purchasemanager(lib.BasePage):
    ID_USERNAME = "login"
    ID_PASSWORD = "password"
    CSS_SUBMIT="button.btn.btn-primary"

    def __init__(self, driver):
        super().__init__(driver)


    def login_purchasemanager(self,username,password):
        time.sleep(1)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//a/span[contains(text(),"Kumaran")]')))
        self.driver.find_element_by_xpath('//a/span[contains(text(),"Kumaran")]').click()
        self.driver.find_element_by_xpath('//a[contains(text(),"Log out")]').click()
        time.sleep(1)
        self.driver.find_element_by_id(self.ID_USERNAME).send_keys(username)
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id(self.ID_PASSWORD).send_keys(password)
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_css_selector(self.CSS_SUBMIT).click()

    def create(self):
        time.sleep(0.4)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Create")]')))
        
        self.driver.find_element_by_xpath('//button[contains(text(),"Create")]').click()

    def vendor(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//input[@class='o_input ui-autocomplete-input']").clear()
        self.driver.find_element_by_xpath("//input[@class='o_input ui-autocomplete-input']").send_keys("Asife")
        self.driver.find_element_by_xpath('//a[contains(text(),"Asife")]').click()


    def add_item(self):
        time.sleep(0.5)
        # WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Add an item')))
        time.sleep(0.5)
        self.driver.find_element_by_link_text("Add an item").click()    

    def add_product(self):
        time.sleep(0.5)
        product_name =["[RM_SF_KALAVAN] Raw Kalavan",
                        "[RM_SF_SEER] Vanjaram/Seer Fish Slices- Raw Mat"]
        quantity=["10","10"]
        for i in range(0,2):
            time.sleep(0.6)
            Purchasemanager.add_item(self)
            time.sleep(0.5)
            self.driver.find_element_by_css_selector("div[name=\"product_id\"] > div.o_input_dropdown > input.o_input.ui-autocomplete-input").clear()
            self.driver.find_element_by_css_selector("div[name=\"product_id\"] > div.o_input_dropdown > input.o_input.ui-autocomplete-input").send_keys(product_name[i])
            time.sleep(0.3)
            WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.LINK_TEXT,''+product_name[i]+'')))
            time.sleep(0.5)
            self.driver.find_element_by_link_text(product_name[i]).click()
            time.sleep(0.3)
            Purchasemanager.change_qunatity(self,quantity[i])
            time.sleep(0.5)

    def change_qunatity(self,quantity):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.NAME, 'product_qty')))
        time.sleep(0.5)
        self.driver.find_element_by_name("product_qty").click()
        self.driver.find_element_by_name("product_qty").clear()
        self.driver.find_element_by_name("product_qty").send_keys(quantity)

    # def save(self):
    #     time.sleep(0.5)
    #     WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH,'(//button[@type="button"])[9]')))
    #     self.driver.find_element_by_xpath("(//button[@type='button'])[9]").click()

    def confirmorder(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[5]')))
        
        self.driver.find_element_by_xpath("//button[5]").click()

    def get_po(self):
        time.sleep(1)
        global po
        po=self.driver.find_element_by_name("name").text
        return po

    def received_product(self):
        time.sleep(1)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[9]')))
        
        self.driver.find_element_by_xpath("//button[9]").click()

    def vendor_bill(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.NAME, 'vendor_reference')))
        
        self.driver.find_element_by_name("vendor_reference").click()
        self.driver.find_element_by_name("vendor_reference").clear()
        self.driver.find_element_by_name("vendor_reference").send_keys("123123")
        
    def update_screenshot(self,scannedbill):
        time.sleep(0.4)
        self.driver.find_element_by_css_selector("div.o_hidden_input_file.o_hidden > form.o_form_binary_form > input[name=\"ufile\"]").send_keys(scannedbill)
    

    def click_attach(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.NAME, 'action_attach_bill')))
        
        time.sleep(0.5)
        self.driver.find_element_by_name("action_attach_bill").click()

    def receive_Products(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Receive Products")]')))
        
        self.driver.find_element_by_xpath('//button[contains(text(),"Receive Products")]').click()


    def edit(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Edit")]')))
     
        self.driver.find_element_by_xpath('//button[contains(text(),"Edit")]').click()

    def done_quantity(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]").click()
        self.driver.find_element_by_name("quantity_done").clear()
        self.driver.find_element_by_name("quantity_done").send_keys("10")
        time.sleep(1)
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]").click()
        time.sleep(0.3)
        self.driver.find_element_by_name("quantity_done").clear()
        self.driver.find_element_by_name("quantity_done").send_keys("10")

    def save(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//button[contains(text(),"Save")]').click()

    def validate(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//button[contains(text(),"Validate")]').click()
        time.sleep(0.5)