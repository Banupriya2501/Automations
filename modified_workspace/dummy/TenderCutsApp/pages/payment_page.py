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
    CSS_CASHONDELIVERY = "ion-item.payment >ion-radio.radio"
    CSS_CASHONDELIVERY1="ion-col.card>ion-row.row>ion-col.col >ion-item.item >ion-radio.radio>button"
    CSS_PLACEORDER = "#placeOrder-btn"
    CSS_CONTINUESHOPPING = ".footer > button#continue-shopping-btn"
    CSS_CONTINUESHOPPING1 = ".footer > button"
    CSS_CHICKEN_IMAGE = "#cat-4"
    XPATH_CVV = "//input[@placeholder='CVV']"
    CSS_CVV = "#payment-mode-cvv-14 > input"
    CSS_CVV1 = "#cvv"
    UIAUTOMATOR_Success = 'new UiSelector().text("Success")'
    CSS_RETRY_PAYMENT =".alert-button-group > button.disable-hover.alert-button.alert-button-md.block-button-top"
    CSS_RETRY_PAYMENT_COD =".alert-button-group > button + button"    
    CSS_NEWCARD = "body > ion-app > ng-component > ion-nav > page-payment > ion-content > div.scroll-content > ion-grid > ion-row:nth-child(2) > ion-card > ion-row > div > ion-icon.icon.icon-md.ion-ios-arrow-forward-outline"
    CSS_ADDNEWCARDS = "ion-card.credit-card-con > ion-row > div.add-card-con"
    CSS_ADDNEWCARD = "#submit-btn"
    CSS_MMYY = "#expiry > input"
    CSS_CARDNO = "#cardno > input"
    CSS_CSHOPPING = "#continue-shopping-btn"
    CSS_PAYTMICON = "#payment-mode-item-13"

    def __init__(self, driver):
        super().__init__(driver)

    def click_cod(self):
        """
        wait for the visiblity and click cod radio button

        """
        
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
        

    def click_card(self):
        """
        wait for the visiblity of card
        and click cvv and pass value

        """
        time.sleep(3)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_CASHONDELIVERY1)))
            # result = self.driver.find_element_by_css_selector(self.CSS_CASHONDELIVERY1).is_displayed()
            # if result == True:
            self.driver.find_element_by_css_selector(self.CSS_CASHONDELIVERY1).click()
            time.sleep(0.4)
            self.driver.find_element_by_xpath(self.XPATH_CVV).send_keys("111")
            # self.driver.find_element_by_css_selector('.cvv-con > ion-input >input.text-input').send_keys('111')
            time.sleep(0.2) 
            # else:
                # print("else condition")
            result = self.driver.find_element_by_css_selector(self.CSS_CASHONDELIVERY1).is_displayed()
            if result == True:
                self.driver.find_element_by_css_selector(self.CSS_CASHONDELIVERY1).click()
                time.sleep(0.4)
                self.driver.find_element_by_css_selector(self.CSS_CVV).click()
                #self.driver.find_element_by_css_selector('#payment-mode-cvv-14 > input').send_keys('111')
                self.driver.find_element_by_css_selector('.cvv-con > ion-input >input.text-input').send_keys('111')
                time.sleep(0.2)
                
            else:
                print()
        except:
            print("not clicked")
        time.sleep(3)

    def click_card1(self):
        """
        wait for the visiblity of card
        and click cvv and pass value

        """
        self.driver.find_element_by_css_selector(self.CSS_CVV1).click()
        self.driver.find_element_by_css_selector("#cvv > input").send_keys('111')
                
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
        time.sleep(0.4)
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

    def add_card(self):
        """
        add new card
        """
        time.sleep(0.5)
        self.driver.implicitly_wait(10)
        card=self.driver.find_element_by_css_selector(self.CSS_ADDNEWCARDS)
        action = TouchActions(self.driver)
        action.tap(card).perform()

    def card_number(self, card):
        time.sleep(0.5)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_CARDNO)))
        self.driver.find_element_by_css_selector(self.CSS_CARDNO).send_keys("4")
        # self.driver.press_keycode(11);
        self.driver.press_keycode(9);
        self.driver.press_keycode(11);
        self.driver.press_keycode(9);
        time.sleep(0.2)
        self.driver.press_keycode(11);
        self.driver.press_keycode(9);
        self.driver.press_keycode(11);
        self.driver.press_keycode(9);
        time.sleep(0.2)
        self.driver.press_keycode(11);
        self.driver.press_keycode(9);
        self.driver.press_keycode(11);
        self.driver.press_keycode(9);
        time.sleep(0.2)
        self.driver.press_keycode(11);
        self.driver.press_keycode(9);
        self.driver.press_keycode(11);
        self.driver.press_keycode(9);
    
    def month_year(self, mmyy):
        time.sleep(0.3)
        self.driver.implicitly_wait(7)
        self.driver.find_element_by_css_selector(self.CSS_MMYY).send_keys("12")
        self.driver.press_keycode(191);
        self.driver.press_keycode(9);
        self.driver.press_keycode(9);

    def save_card(self):
        time.sleep(0.6)
        self.driver.implicitly_wait(7)
        self.driver.find_element_by_css_selector(self.CSS_ADDNEWCARD).click()

    def paytm_icon(self):
        time.sleep(5)
        self.driver.find_element_by_css_selector(self.CSS_PAYTMICON).click()

    def paytm_back(self):
        time.sleep(1.5)
        self.driver.implicitly_wait(7)
        self.driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-nav/page-payment/ion-header/ion-navbar/button").click()

    def pay_back(self):
        time.sleep(1.5)
        self.driver.implicitly_wait(7)
        self.driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-nav/page-payment/ion-header/ion-navbar/button").click()

    def deli_back(self):
        time.sleep(1.3)
        self.driver.implicitly_wait(7)
        self.driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-nav/page-delivery-summary/ion-header/ion-navbar/button").click()

    def cart_back(self):
        time.sleep(1.3)
        self.driver.implicitly_wait(7)
        self.driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-nav/page-cart-summary/ion-header/ion-navbar/button").click()

    def cshopping(self):
        time.sleep(1.3)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector(self.CSS_CSHOPPING).click()






        
        
