
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


class Manufacturepage(lib.BasePage):
    ID_USERNAME = "login"
    ID_PASSWORD = "password"
    CSS_SUBMIT="button.btn.btn-primary"

    def __init__(self, driver):
        super().__init__(driver)


    def humbergermenu(self):
        import pdb
        pdb.set_trace()
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//nav[2]/div/div/a/i')))
        self.driver.find_element_by_xpath("//nav[2]/div/div/a/i").click()
    
    def manufacture_app(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("//img[@alt='Manufacturing']").click()

    def create(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("(//button[@type='button'])[7]").click()

    def product(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[6]/table[1]/tbody/tr[4]/td[2]/div/div/input").click()
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[6]/table[1]/tbody/tr[4]/td[2]/div/div/input").clear()
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[6]/table[1]/tbody/tr[4]/td[2]/div/div/input").send_keys("1026")
        self.driver.find_element_by_link_text("[RM_MRT_CLASSIC_BBQ_WINGS,1026] Bbq Wings").click()
        
    def quantitytoproduce(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_name("product_qty").click()
        self.driver.find_element_by_name("product_qty").clear()
        self.driver.find_element_by_name("product_qty").send_keys("10")

    def save(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("(//button[@type='button'])[9]").click()
        
    def create_workspace(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("//button[5]").click()

    def workspace(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("//div[4]/button").click()
       
    def package(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_css_selector("td.o_data_cell.o_readonly_modifier").click()

    def startworking(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("//div[2]/div/button[3]").click()

    def edit(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("(//button[@type='button'])[7]").click()

    def totaltield(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_name("total_yield").click()
        self.driver.find_element_by_name("total_yield").clear()
        self.driver.find_element_by_name("total_yield").send_keys("10")

    def barcode(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_name("plu_code").click()
        self.driver.find_element_by_name("plu_code").clear()
        self.driver.find_element_by_name("plu_code").send_keys("10010220180724")
        self.driver.find_element_by_name("plu_code").send_keys(Keys.ENTER)

    def enter_weight(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_id("weightField").click()
        self.driver.find_element_by_id("weightField").clear()
        self.driver.find_element_by_id("weightField").send_keys("10")
        self.driver.find_element_by_xpath("html/body/div[6]/div/div/div[3]/button").click()


    def lot_servial(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[3]/div[3]/div/div[3]/div[3]/div[2]/table/tbody/tr[1]/td[3]").click()
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[3]/div[3]/div/div[3]/div[3]/div[2]/table/tbody/tr[1]/td[3]").send_keys("0000216")

        self.driver.find_element_by_link_text("0000216").click()

    def save_product(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("(//button[@type='button'])[8]").click()
       

    def done(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("//button[4]").click()


    def clickmo(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_link_text("MO/").click()

    def click_workorder(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("//div[4]/button").click()

    def click_package2(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_css_selector("tr.o_data_row.text-danger > td.o_data_cell.o_readonly_modifier").click()
        

    def start_working(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("//div[2]/div/button[3]").click()

    def edit(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("(//button[@type='button'])[7]").click()

    def barcode(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_name("plu_code").click()
        self.driver.find_element_by_name("plu_code").clear()
        self.driver.find_element_by_name("plu_code").send_keys("10011920180724")
        self.driver.find_element_by_name("plu_code").send_keys(Keys.ENTER)

    def wight(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_id("weightField").clear()
        self.driver.find_element_by_id("weightField").send_keys("10")
        self.driver.find_element_by_xpath("(//button[@type='button'])[31]").click()

    def save1(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("(//button[@type='button'])[8]").click()

    def done(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("//button[4]").click()
         
    def manufacturing_order(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_css_selector("ol.breadcrumb > li > a").click()

    def link_one(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("//td[4]").click()

    def mark_as_done(self):
        import pdb
        pdb.set_trace()
        self.driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/button[2]").click()
        self.driver.find_element_by_css_selector("ol.breadcrumb > li > a").click()
    


        
        
       
       
        
        
       
      
       
        
       




        