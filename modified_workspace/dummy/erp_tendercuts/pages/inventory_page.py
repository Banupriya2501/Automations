
"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import select
import lib
import datetime


class Inventorypage(lib.BasePage):
    ID_USERNAME = "login"
    ID_PASSWORD = "password"
    CSS_SUBMIT="button.btn.btn-primary"

    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_adminstrator(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//a/span[contains(text(),"Thoraipakkam Store")]')))
        self.driver.find_element_by_xpath('//a/span[contains(text(),"Thoraipakkam Store")]').click()
        self.driver.find_element_by_xpath('//a[contains(text(),"Log out")]').click()
        time.sleep(1)

    def reporting(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Reporting')))
        self.driver.find_element_by_link_text('Reporting').click()

    def inventory(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Inventory')))
        self.driver.find_element_by_link_text('Inventory').click()

    def current_inventory(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button//span[contains(text(),"Retrieve the Inventory Quantities")]')))
        self.driver.find_element_by_xpath('//button//span[contains(text(),"Retrieve the Inventory Quantities")]').click()

    def filter(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[1]/div[1]/div/span')))
        self.driver.find_element_by_xpath('html/body/div[1]/div/div[1]/div[1]/div/span').click()
       

    def click_filter(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]/button')))
        self.driver.find_element_by_xpath('html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]/button').click()
        
    def click_filter_advance(self):
        today = format(datetime.date.today(), "%y%m%d")

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Add Custom Filter")]')))
        self.driver.find_element_by_xpath('//a[contains(text(),"Add Custom Filter")]').click()

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//select')))
        Select(self.driver.find_element_by_xpath("//select")).select_by_visible_text("Lot/Serial Number")
        Select(self.driver.find_element_by_css_selector("select.o_input.o_searchview_extended_prop_op")).select_by_visible_text("is equal to")
        self.driver.find_element_by_css_selector("input.o_input").clear()
        self.driver.find_element_by_css_selector("input.o_input").send_keys("THP_RM_SF_ANCHOVY_"+today+"")

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '(//button[@type="button"])[9]')))
        self.driver.find_element_by_xpath("(//button[@type='button'])[9]").click()

    def select_product(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//td[contains(text(),"[RM_SF_ANCHOVY] Nethili - Anchovy - Raw Mat")]')))
        self.driver.find_element_by_xpath('//td[contains(text(),"[RM_SF_ANCHOVY] Nethili - Anchovy - Raw Mat")]').click()

    def quantity(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.NAME, 'quantity')))
        quantity=self.driver.find_element_by_name('quantity').text
        # assert quantity == "90.00"


    def filter_advance(self,productname):
        time.sleep(0.5)
        today = format(datetime.date.today(), "%y%m%d")

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Add Custom Filter")]')))
        self.driver.find_element_by_xpath('//a[contains(text(),"Add Custom Filter")]').click()

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//select')))
        Select(self.driver.find_element_by_xpath("//select")).select_by_visible_text("Lot/Serial Number")
        Select(self.driver.find_element_by_css_selector("select.o_input.o_searchview_extended_prop_op")).select_by_visible_text("is equal to")
        self.driver.find_element_by_css_selector("input.o_input").clear()
        self.driver.find_element_by_css_selector("input.o_input").send_keys("THP_"+productname+"_"+today+"")

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '(//button[@type="button"])[9]')))
        self.driver.find_element_by_xpath("(//button[@type='button'])[9]").click()

    def click_product(self,productname):
        time.sleep(0.5)
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//td[contains(text(),"[RM_SF_ANCHOVY] Nethili - Anchovy - Raw Mat")]')))
        self.driver.find_element_by_xpath("//td[2][contains(text(),"+productname+")]").click()

    def group_by(self):
        time.sleep(0.3)
        self.driver.find_element_by_css_selector("span.o_searchview_more.fa").click()
