"""
this module to verify cartsummary page
"""
import time

from selenium.webdriver.common.touch_actions import TouchActions

import lib


class CartSummaryPage(lib.BasePage):
    BY_NAME_PROCEED = "ios-cart"
    BY_NAME_CHECKOUT = "md-done-all"
    CSS_SELECTDELIVERTTIME = "#undefined"
    CSS_INCREASEQUANTITY =".grid > ion-row > ion-col + ion-col > button#increase-button-CHK_WHL_SKIN_OFF"

    def __init__(self, driver):
        super().__init__(driver)

    def click_proceed(self):
        """
        click proceed button

        """
        time.sleep(3)
        self.driver.implicitly_wait(10)
        # proceedbutton=self.driver.find_element_by_css_selector('ion-footer.footer > tcuts-cart > ion-row#cart-proceed-button > ion-col > ion-icon.ng-tns-c3-3')

        proceedbutton = self.driver.find_element_by_name(self.BY_NAME_PROCEED)
        action = TouchActions(self.driver)
        action.tap(proceedbutton).perform()

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
        time.sleep(5)
        self.driver.implicitly_wait(10)
        checkout = self.driver.find_element_by_name(self.BY_NAME_CHECKOUT)
        action = TouchActions(self.driver)
        action.tap(checkout).perform()

    def verify_deliverypage(self):
        """
        verify it redirect to deliverysummary page

        """
        time.sleep(1)
        self.driver.implicitly_wait(7)
        result = self.driver.find_element_by_css_selector(self.CSS_SELECTDELIVERTTIME).is_displayed()
        assert (True == result)

    def increase_product(self,quantity):
        """
        increase the product quantity for chicken

        """
        time.sleep(1)
        self.driver.implicitly_wait(7)
        i = 1
        while i < int(quantity):
            time.sleep(4)
            chickenwholeoff = self.driver.find_element_by_css_selector(self.CSS_INCREASEQUANTITY)
            action = TouchActions(self.driver)
            action.tap(chickenwholeoff).perform()
            i = i + 1

    def cart_product_add(self,quantity):
        i = 1
        while i < int(quantity):
            time.sleep(4)
            # chickenwholeoff = self.driver.find_element_by_xpath('//*[contains(@id,"increase-button-CHK_WHL_SKIN_OFF")]')

            parentelement = self.driver.find_element_by_css_selector('ion-card.products > tcuts-product > ion-grid.listing > ion-row > ion-col + ion-col + ion-col >tcuts-counter >.grid > ion-row > ion-col + ion-col > button')
            # childelement=self.driver.find_element_by_xpath('//*[contains(@id,"increase-button-CHK_WHL_SKIN_OFF")]')
            action = TouchActions(self.driver)
            action.tap(parentelement).perform()
            time.sleep(4)
            i = i + 1