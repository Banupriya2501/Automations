"""
this module to verify and select product from category page
"""
import time

from selenium.webdriver.common.touch_actions import TouchActions

import lib


class Categorypage(lib.BasePage):
    CSS_ADD_BUTTON_CHICKENN = "#add-button-CHK_WHL_SKIN_OFF "
    CSS_ADD_GOAT="#add-button-GT_BIRYANI_CUT "
    CSS_ADD_BUTTON_CHICKEN1 = ".add"
    CSS_ADD_BUTTON_MARINADES = "#add-button-MRT_KOLA_URUNDAI"
    BY_NAME_PROCEED = "ios-cart"
    CSS_ADD_BUTTON_INCREMENT ="#increase-button-CHK_WHL_SKIN_OFF"  
    CSS_ADD_BUTTON_INCREMENT1 ="#increase-button-MRT_KOLA_URUNDAI"
    CSS_OUTOFSTOCK =".alert-head"

    def __init__(self, driver):
        super().__init__(driver)

    def click_product_add(self, product):
        """
        if [product] is chicken click chicekn whole off or else
        if marinades click kola product and add to cart
        :param product: passing chicken or marinades

        """
        time.sleep(0.5)
        if product == "chicken":
            time.sleep(1)
            # self.driver.implicitly_wait(15)
            wholeoff = self.driver.find_element_by_css_selector(self.CSS_ADD_BUTTON_CHICKENN)
            action = TouchActions(self.driver)
            action.tap(wholeoff).perform()
        elif product == "marinades":
            # next1 = self.driver.find_element_by_css_selector('#next-category-button')
            # action = TouchActions(self.driver)
            # action.tap(next1).perform()
            marinadesicon = self.driver.find_element_by_css_selector('.category-row > div#category-item-5')
            action = TouchActions(self.driver)
            action.tap(marinadesicon).perform()
            self.driver.implicitly_wait(30)
            kola = self.driver.find_element_by_css_selector(self.CSS_ADD_BUTTON_MARINADES)
            action = TouchActions(self.driver)
            action.tap(kola).perform()

    def add_one(self,quantity):
        """
        increase one quantity for the product
        """
        i = 1
        while i < int(quantity):
            time.sleep(0.4)
            try:
                chickenwholeoff = self.driver.find_element_by_css_selector('ion-grid > ion-row >ion-col + ion-col > button#increase-button-CHK_WHL_SKIN_OFF')
            except:
                chickenwholeoff = self.driver.find_element_by_css_selector(self.CSS_ADD_BUTTON_INCREMENT1)
            action = TouchActions(self.driver)
            action.tap(chickenwholeoff).perform()
            i = i + 1

    def verify_proceedbutton(self):
        """
        Verify proceed button displays after adding product to cart

        """
        self.driver.implicitly_wait(7)
        result = self.driver.find_element_by_name(self.BY_NAME_PROCEED).is_displayed()
        assert (True == result)

    def verify_outofstockalert(self):
        """
        check out of stock alert
        """

        self.driver.implicitly_wait(7)
        result = self.driver.find_element_by_css_selector(self.CSS_OUTOFSTOCK).is_displayed()

