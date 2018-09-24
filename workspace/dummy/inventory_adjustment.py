
"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Inventory_adjustmentpage(lib.BasePage):
    ID_USERNAME = "login"
    ID_PASSWORD = "password"
    CSS_SUBMIT="button.btn.btn-primary"

    def __init__(self, driver):
        super().__init__(driver)


    def clear_inventory(self):

      #   # //Humbermenu
      #   self.driver.find_element_by_xpath("//nav[2]/div/div/a/i").click()
      # # //INTORYAPP
       
      #   self.driver.find_element_by_xpath("//img[@alt='Inventory']").click()
      # # //operation
      
      #   self.driver.find_element_by_linktext("Operations").click()
      #   # //inventoryAdjust
      
      #   self.driver.find_element_by_xpath("//div[@id='odooMenuBarNav']/div/div/ul[4]/li[4]/ul/li[3]/a/span").click()
      #   # //create
        
      #   self.driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
      #   # //enter value
       
      #   self.driver.find_element_by_xpath("//input[@class='o_field_char o_field_widget o_input o_required_modifier']").click()
      #   self.driver.find_element_by_xpath("//input[@class='o_field_char o_field_widget o_input o_required_modifier']").clear()
      #   self.driver.find_element_by_xpath("//input[@class='o_field_char o_field_widget o_input o_required_modifier']").send_keys("vvv")
       
      #   # //list search 
      #   self.driver.find_element_by_xpath("//div/input[1][@class='o_input ui-autocomplete-input']").clear()
      #   # //driver.findElement(By.xpath("//div/input[1][@class='o_input ui-autocomplete-input']").click()
      
      #   self.driver.find_element_by_xpath("//div/input[1][@class='o_input ui-autocomplete-input']").send_keys("VWK")
      #   # //driver.findElement(By.xpath("//div/input[1][@class='o_input ui-autocomplete-input']").click()
      #   self.driver.find_element_by_xpath("//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li").click()