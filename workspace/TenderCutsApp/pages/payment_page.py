"""
This module to check payement page
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from appium import webdriver

import lib


class PaymentPage(lib.BasePage):
    CSS_CASHONDELIVERY = "#payment-mode-radio-0"
    CSS_CASHONDELIVERY1 = "#payment-mode-item-4"
    CSS_PLACEORDER = "#placeOrder-btn"
    CSS_CONTINUESHOPPING = ".footer > button#continue-shopping-btn"
    CSS_CONTINUESHOPPING1 = ".footer > button"
    CSS_CHICKEN_IMAGE = "#cat-4"
    CSS_CVV = "#payment-mode-cvv-4"
    CSS_SUCCESS = 'new UiSelector().description("Success")'
    UIAUTOMATOR_Success = 'new UiSelector().text("Success")'
    CSS_RETRY_PAYMENT =".alert-button-group > button.disable-hover.alert-button.alert-button-md.block-button-top"
    CSS_RETRY_PAYMENT_COD =".alert-button-group > button + button"

    def __init__(self, driver):
        super().__init__(driver)

    def click_cod(self):
        """
        wait for the visiblity and click cod radio button

        """
        time.sleep(6)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_CASHONDELIVERY)))
            result = self.driver.find_element_by_css_selector(self.CSS_CASHONDELIVERY).is_displayed()
            if result == True:
                self.driver.find_element_by_css_selector(self.CSS_CASHONDELIVERY).click()
            else:
                print('Not visible')
        except:
            print()
        time.sleep(3)

    def click_card(self):
        """
        wait for the visiblity of card
        and click cvv and pass value

        """
        time.sleep(3)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_CASHONDELIVERY1)))
            result = self.driver.find_element_by_css_selector(self.CSS_CASHONDELIVERY1).is_displayed()
            if result == True:
                self.driver.find_element_by_css_selector(self.CSS_CASHONDELIVERY1).click()
                time.sleep(4)
                self.driver.find_element_by_css_selector(self.CSS_CVV).click()
                self.driver.find_element_by_css_selector('.cvv-con > ion-input >input.text-input').send_keys('111')
                time.sleep(2)
                
            else:
                print()
        except:
            print()
        time.sleep(3)

    def card_success(self): 
        """
        click success button from razor pay
        """          
        handles = self.driver.window_handles
        while len(handles) != 3:
            handles = self.driver.window_handles
        self.driver.switch_to_window(handles[2])
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.success')))        
        self.driver.find_element_by_class_name("success").click()
        self.driver.switch_to_window(handles[0])

    def card_failure(self):     
        """
        click failure button from razor pay
        """        
        handles = self.driver.window_handles
        while len(handles) != 3:
            handles = self.driver.window_handles
        self.driver.switch_to_window(handles[2])        
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.success')))
        self.driver.find_element_by_class_name("danger").click()
        self.driver.switch_to_window(handles[0])

    def click_place_order(self):
        """
        click place order button
        """
        WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_PLACEORDER)))
        placeorder = self.driver.find_element_by_css_selector(self.CSS_PLACEORDER)
        action = TouchActions(self.driver)
        action.tap(placeorder).perform()

    def get_orderno(self):
        """
        get card number from continue shopping page
        """
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#order-no')))
        order_id=self.driver.find_element_by_css_selector('#order-no').text
        return order_id

    def click_placeorder(self):
        """
        click place order button

        """
        time.sleep(4)
        placeorder = self.driver.find_element_by_css_selector(self.CSS_PLACEORDER)
        action = TouchActions(self.driver)
        action.tap(placeorder).perform()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#order-no')))
        order_id=self.driver.find_element_by_css_selector('#order-no').text
        return order_id


    def click_continueshopping(self):
        """
        click continue shopping button
        """
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_CONTINUESHOPPING1)))
        self.driver.find_element_by_css_selector(self.CSS_CONTINUESHOPPING1).is_displayed()
        continueshopping = self.driver.find_element_by_css_selector(self.CSS_CONTINUESHOPPING1)
        action = TouchActions(self.driver)
        action.tap(continueshopping).perform()

    def paymentfail_retry(self): 
        """
        retry option
        """   
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_RETRY_PAYMENT)))
        self.driver.find_element_by_css_selector(self.CSS_RETRY_PAYMENT).send_keys(Keys.ENTER)
        # self.driver.find_element_by_name("plu_code").send_keys(Keys.ENTER)
        time.sleep(4)

    def paymentfailed_cod(self):
        """
        click cod in retry option
        """
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_RETRY_PAYMENT_COD)))
        self.driver.find_element_by_css_selector(self.CSS_RETRY_PAYMENT_COD).click()
        time.sleep(4)

    def outofstock_pop(self):
        """
        check out of stock popup
        """
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button#close-button')))
        popup=self.driver.find_element_by_css_selector('button#close-button')
        action = TouchActions(self.driver)
        action.tap(popup).perform()