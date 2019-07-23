"""
This module to verify rating
"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib

class Ratingpage(lib.BasePage):
    CSS_STAR = "#tabpanel-t0-0 > page-home > ion-footer > tcuts-order-rating > div > ion-row > ion-col:nth-child(1) > ion-row:nth-child(2) > ion-icon:nth-child(5)"
    CSS_TASTE = "body > ion-app > ion-modal > div > page-rating-review > ion-content > div.scroll-content > div.custom-alert > div > div > ion-scroll > div > div > div:nth-child(1) > button"
    CSS_QUALITY = "body > ion-app > ion-modal > div > page-rating-review > ion-content > div.scroll-content > div.custom-alert > div > div > ion-scroll > div > div > div:nth-child(2) > button"
    CSS_COMMENTS = "body > ion-app > ion-modal > div > page-rating-review > ion-content > div.scroll-content > div.custom-alert > div > div > ion-list > ion-item > div.item-inner > div > ion-textarea > textarea"
    CSS_SUBMIT = "#submit-button"
    CSS_RATE = "body > ion-app > ion-alert > div > div.alert-button-group > button.disable-hover.alert-button.alert-button-md.block-button-top.alert-button-default.alert-button-default-md.ng-star-inserted"



    def __init__(self, driver):
        super().__init__(driver)

    def click_star(self):
    	time.sleep(5)
    	self.driver.implicitly_wait(7)
    	self.driver.find_element_by_css_selector(self.CSS_STAR).click()

    def click_taste(self):
    	time.sleep(5)
    	self.driver.implicitly_wait(7)
    	self.driver.find_element_by_css_selector(self.CSS_TASTE).click()

    def click_quality(self):
    	time.sleep(5)
    	self.driver.implicitly_wait(7)
    	self.driver.find_element_by_css_selector(self.CSS_QUALITY).click()

    def enter_comments(self):
    	time.sleep(5)
    	self.driver.implicitly_wait(7)
    	self.driver.find_element_by_css_selector(self.CSS_COMMENTS).send_keys('The product which i ordered Is good. It Is very Tasty And Quality too. With On Time Delivary. Very Resonable price with goof non-veg chain')

    def click_submit(self):
    	time.sleep(5)
    	self.driver.implicitly_wait(7)
    	self.driver.find_element_by_css_selector(self.CSS_SUBMIT).click()

    def click_rate(self):
    	time.sleep(5)
    	self.driver.implicitly_wait(7)
    	self.driver.find_element_by_css_selector(self.CSS_RATE).click()
    	time.sleep(15)

