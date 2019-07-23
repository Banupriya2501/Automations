"""
this module to verify cartsummary page
"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class CartSummaryPage(lib.BasePage):
    BY_NAME_PROCEED="ion-fab.checkout-button > button"
    BY_NAME_CHECKOUT = "md-done-all"
    CSS_SELECTDELIVERTTIME = "#undefined"
    CSS_INCREASEQUANTITY =".grid > ion-row > ion-col + ion-col > button#increase-button-CHK_WHL_SKIN_OFF"
    CSS_COUPONTAB = "#tab-coupon-button"
    CSS_COUPONCODE = "#coupon-code > input"
    CSS_COUPONAPPLY = "#coupon-apply-button"
    CSS_COUPONOK = "#ok-button"
    CSS_REMOVECODE = "#coupon-apply-button"
    CSS_LOADER="div >div.loading-spinner >ion-spinner.spinner"
    CSS_PROCEED="#cart-proceed-button"

    def __init__(self, driver):
        super().__init__(driver)

    def click_proceed(self):
        """
        click proceed button

        """

        time.sleep(0.3)
        # self.driver.implicitly_wait(10)
        # proceedbutton=self.driver.find_element_by_css_selector('ion-footer.footer > tcuts-cart > ion-row#cart-proceed-button > ion-col > ion-icon.ng-tns-c3-3')
        self.driver.find_element_by_css_selector(self.BY_NAME_PROCEED).click()
        # proceedbutton = self.driver.find_element_by_name(self.BY_NAME_PROCEED)
        # action = TouchActions(self.driver)
        # action.tap(proceedbutton).perform()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.CSS_LOADER)))

    def click_proceed_search(self):
        time.sleep(0.3)
        proceedbutton = self.driver.find_element_by_css_selector(self.CSS_PROCEED)
        action = TouchActions(self.driver)
        action.tap(proceedbutton).perform()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.CSS_LOADER)))

       


    def verify_checkoutpage(self):
        """
        verify checkout page displays
        """

        time.sleep(5)
        self.driver.implicitly_wait(7)
        result = self.driver.find_element_by_name(self.BY_NAME_CHECKOUT).is_displayed()
        assert (True == result)

    def click_checkout(self):
        """
        click checkout button

        """
        checkout = self.driver.find_element_by_name(self.BY_NAME_CHECKOUT)
        action = TouchActions(self.driver)
        action.tap(checkout).perform()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.CSS_LOADER)))


    def verify_deliverypage(self):
        """
        verify it redirect to deliverysummary page

        """
    
        self.driver.implicitly_wait(7)
        result = self.driver.find_element_by_css_selector(self.CSS_SELECTDELIVERTTIME).is_displayed()
        assert (True == result)

    def increase_product(self,quantity):
        """
        increase the product quantity for chicken

        """
        time.sleep(0.5)
        self.driver.implicitly_wait(7)
        i = 1
        while i < int(quantity):
            # time.sleep(6)
            chickenwholeoff = self.driver.find_element_by_css_selector(self.CSS_INCREASEQUANTITY)
            action = TouchActions(self.driver)
            action.tap(chickenwholeoff).perform()
            i = i + 1

    def cart_product_add(self,quantity):
        i = 1
        while i < int(quantity):
            
            # chickenwholeoff = self.driver.find_element_by_xpath('//*[contains(@id,"increase-button-CHK_WHL_SKIN_OFF")]')

            parentelement = self.driver.find_element_by_css_selector('ion-card.products > tcuts-product > ion-grid.listing > ion-row > ion-col + ion-col + ion-col >tcuts-counter >.grid > ion-row > ion-col + ion-col > button')
            # childelement=self.driver.find_element_by_xpath('//*[contains(@id,"increase-button-CHK_WHL_SKIN_OFF")]')
            action = TouchActions(self.driver)
            action.tap(parentelement).perform()
            WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.CSS_LOADER)))
            i = i + 1
            

    def coupon_tab(self):
        time.sleep(5)
        self.driver.find_element_by_css_selector(self.CSS_COUPONTAB).click()

    def coupon_code(self, coupon):
        time.sleep(1.5)
        self.driver.find_element_by_css_selector(self.CSS_COUPONCODE).send_keys(coupon)
        time.sleep(0.8)
        apply_button=self.driver.find_element_by_css_selector(self.CSS_COUPONAPPLY)
        action = TouchActions(self.driver)
        action.tap(apply_button).perform()
        time.sleep(0.8)
        ok_button=self.driver.find_element_by_css_selector(self.CSS_COUPONOK)
        action = TouchActions(self.driver)
        action.tap(ok_button).perform()

    def remove_code(self):
        
        remove_button=self.driver.find_element_by_css_selector(self.CSS_REMOVECODE)
        action = TouchActions(self.driver)
        action.tap(remove_button).perform()

