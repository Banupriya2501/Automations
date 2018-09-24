"""

This module to check signin functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import lib


class Orderpickerpage(lib.BasePage):
    CSS_ORDERID = "#order_id > input"
    CSS_SEARCH= ".form > ion-row > ion-col + ion-col > button"
    CSS_ASSIGN=".card > ion-grid.order-grid"
    CSS_ALERT=".alert-button-group > button + button"
    CSS_BARCODE=".barcode-text > input"
    CSS_DONE=".barcode-pen"
    CSS_ASSIGNORDER=".assign-order"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_orderid(self,orderid):
        
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_ORDERID)))
        time.sleep(0.5)
        self.driver.find_element_by_css_selector(self.CSS_ORDERID).send_keys(orderid)

    def click_search(self):
        time.sleep(1)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_SEARCH)))

        self.driver.find_element_by_css_selector(self.CSS_SEARCH).click()
        time.sleep(15)

    def assignorder(self):
        time.sleep(1)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_ASSIGN)))
        self.driver.find_element_by_css_selector(self.CSS_ASSIGN).click()

    def alert(self):
  
        time.sleep(2)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_ALERT)))

        self.driver.find_element_by_css_selector(self.CSS_ALERT).click()

    def barcode(self):
        
        time.sleep(5)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_BARCODE)))

        self.driver.find_element_by_css_selector(self.CSS_BARCODE).send_keys("19300500")

    def done(self):
        
        time.sleep(5)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_DONE)))

        donebutton=self.driver.find_element_by_css_selector(self.CSS_DONE)
        action = TouchActions(self.driver)
        action.tap(donebutton).perform()

    def assign(self):
      
        time.sleep(5)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_ASSIGNORDER)))

        self.driver.find_element_by_css_selector(self.CSS_ASSIGNORDER).click()

    def toastmsg(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.toast-message')))
        toast=self.driver.find_element_by_css_selector('.toast-message').text
        assert toast == "Order Assigned Successfully"

    def donebutton(self):
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button#cancel-button')))   
        self.driver.find_element_by_css_selector('button#cancel-button').click()

    def completeorder(self):
        
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_ASSIGN)))   
        
        self.driver.find_element_by_css_selector(self.CSS_ASSIGN).click()

    def complete_the_order(self):
       
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.button_complete')))   
        self.driver.switch_to.context('NATIVE_APP')
        self.driver.set_location(80, 12, 00)
        self.driver.switch_to.context('WEBVIEW_com.tendercuts.driver')
        self.driver.find_element_by_css_selector('button.button_complete').click()

    def toast_msg(self):
        
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.toast-message')))
        toast=self.driver.find_element_by_css_selector('.toast-message').text
        assert toast == "Order Completed Successfully"

    def complete_later(self):
        time.sleep(1)
        import pdb
        pdb.set_trace()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#complete-later-btn-0')))
        self.driver.find_element_by_css_selector('#complete-later-btn-0').click()

    def toastmessage(self):
       
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.toast-message')))
        toast=self.driver.find_element_by_css_selector('.toast-message').text
        assert toast == 'Order Completed Successfully'