
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


    def check_inventory(self):
		# self.driver.find_element_by_xpath("//nav[2]/div/div/a/i").click()
		#     # //inventory app
		    
		# self.driver.find_element_by_xpath("//img[@alt='Inventory']").click()
		#     # //report
		   
		# self.driver.find_element_by_xpath("(//a[contains(text(),'Reporting')])[2]").click()
		#     # //Inventory click
		    
		# self.driver.find_element_by_xpath("//div[@id='odooMenuBarNav']/div/div/ul[5]/li[7]/ul/li/a/span").click()
		#     # //inventory date
		    
		# self.driver.find_element_by_name("open_table").click()
		#     # //close
		    
		# self.driver.find_element_by_xpath("//div/div[2]/div[2]").click()
		#     # //close
		    
		# self.driver.find_element_by_xpath("//div/div/div/div/div[2]").click()
		#     # //+ button
		    
		# self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[1]/div/span").click()
		#     # //groupby click
		    
		# self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[3]/div[1]/div[2]/button").click()
		#     # //location
		    
		# self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[3]/div[1]/div[2]/ul/li[1]/a").click()
		#     # //purch/stock
		    
		# self.driver.find_element_by_xpath("//tr//th[text()[contains(.,'PURCH')]]").click()
		#     # //gt_carcass
		    
		#     boolean present=self.driver.find_element_by_xpath("//tr//td[text()[contains(.,'GT_CARCASS')]]"))!= null;
		   
		#     if present==true
		    
		#     	# System.out.println("PRODUCT UPDATED");
		#     	self.driver.find_element_by_xpath("//tr//td[text()[contains(.,'Goat Carcass')]]").click()
		    	   
		#     	String quantity=driver.findElement(By.xpath("//span[@name='quantity']").text
		    
		#     	if(quantity.equals("125.00"))
		    	
		#     		# System.out.println("PRODUCT GT_CARCASS UPDATED in PURCH/STOCK");
		    		
		# 		    self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ol/li[2]/a").click()
		    		
		    	