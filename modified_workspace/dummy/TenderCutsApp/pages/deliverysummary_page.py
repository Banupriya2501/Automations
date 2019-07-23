"""
This module to verify deliverysummary page
"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import lib


class DeliverySummaryPage(lib.BasePage):
    CSS_SELECTDELIVERTTIME = "#undefined"
    CSS_EXPRESSDELIVERY = "#alert-input-0-2"
    CSS_EXPRESSDELIVERY1 = "#alert-input-1-2"
    CSS_OK = ".alert-button-group > button + button"
    CSS_SELECTADDRESS = "#address-select-button"
    CSS_ADDRESS = "#deliverable-address-1"
    CSS_CONTINUE = "#continue-button"
    CSS_PLACEORDER = "#placeOrder-btn"
    CSS_SCHEDULETOMORROW = ".convert-button-container"
    CSS_SCHEDULEDELIVERY = "#alert-input-0-2"
    CSS_SCHEDULEDELIVERY1 = "#alert-input-1-2"
    CSS_OUTSIDE_DELIVERY_REGION="#inbound-address-"
    # cant-deliverable-address-1
    CSS_ALERTTOANOTHERSTORE = ".alert-button-group > button +button"
    CSS_LOADER="div >div.loading-spinner >ion-spinner.spinner"



    def __init__(self, driver):
        super().__init__(driver)

    def select_timeslot(self, product):
        """
        click time slot[express delivery] and click ok for chicken
        or else select schedule quantity and cilck ok
        :param product: this variable to verify chicken or marinades

        """
        if product == "chicken":
            # self.driver.implicitly_wait(19)
            self.driver.find_element_by_css_selector(self.CSS_SELECTDELIVERTTIME).click()
            time.sleep(0.2)
            try:
                self.driver.find_element_by_css_selector(self.CSS_EXPRESSDELIVERY).click()
            except:
                self.driver.find_element_by_css_selector(self.CSS_EXPRESSDELIVERY1).click()
            self.driver.find_element_by_css_selector(self.CSS_OK).click()
            WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.CSS_LOADER)))

            
        elif product == "marinades":
            time.sleep(0.2)
            self.driver.implicitly_wait(19)
            torow = self.driver.find_element_by_css_selector(self.CSS_SCHEDULETOMORROW)
            action = TouchActions(self.driver)
            action.tap(torow).perform()
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.CSS_SELECTDELIVERTTIME).click()
            time.sleep(0.5)
            try:
                self.driver.find_element_by_css_selector(self.CSS_SCHEDULEDELIVERY).click()
            except:
                self.driver.find_element_by_css_selector(self.CSS_SCHEDULEDELIVERY1).click()
            
            self.driver.find_element_by_css_selector(self.CSS_OK).click()
            WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.CSS_LOADER)))
            

    def select_address(self):
        """
        click select button and click address option1

        """
        self.driver.implicitly_wait(9)
        option = self.driver.find_element_by_css_selector(self.CSS_SELECTADDRESS)
        action = TouchActions(self.driver)
        action.tap(option).perform()
        time.sleep(1)
        address=self.driver.find_element_by_css_selector(self.CSS_ADDRESS)
        action = TouchActions(self.driver)
        action.tap(address).perform()

    def click_continue(self):
        """
        click continue button

        """
        time.sleep(0.5)
        continuebutton = self.driver.find_element_by_css_selector(self.CSS_CONTINUE)
        action = TouchActions(self.driver)
        action.tap(continuebutton).perform()



    def verify_paymentpage(self):
        """
        verify place order page displays
        """
        self.driver.implicitly_wait(7)
        result = self.driver.find_element_by_css_selector(self.CSS_PLACEORDER).is_displayed()
        assert (True == result)


    def out_delivery_region(self):
        self.driver.implicitly_wait(9)
        option = self.driver.find_element_by_css_selector(self.CSS_SELECTADDRESS)
        action = TouchActions(self.driver)
        action.tap(option).perform()
        time.sleep(1)
        # Result=self.driver.find_element_by_css_selector(self.CSS_OUTSIDE_DELIVERY_REGION).is_displayed()
        try:
            outside_region=self.driver.find_element_by_css_selector(self.CSS_OUTSIDE_DELIVERY_REGION)
            action = TouchActions(self.driver)
            action.tap(outside_region).perform()
        except:
            time.sleep(1)
            newaddress=self.driver.find_element_by_css_selector('#add-new-address-button')
            action = TouchActions(self.driver)
            action.tap(newaddress).perform()
            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#flat-no > input')))
                self.driver.find_element_by_css_selector('ion-input#flat-no >input').send_keys('flatno')
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#street > input')))
                self.driver.find_element_by_css_selector('ion-input#street > input').send_keys('street')
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#landmark > input')))
                self.driver.find_element_by_css_selector('ion-input#landmark > input').send_keys('landmark')
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#pincode > input')))
                self.driver.find_element_by_css_selector('#pincode > input').send_keys('600059')
                update=self.driver.find_element_by_css_selector('#add-new-address-submit')
                action = TouchActions(self.driver)
                action.tap(update).perform()
                time.sleep(3)
                self.driver.switch_to.context('NATIVE_APP')
                try:
                    self.driver.find_element_by_android_uiautomator('new UiSelector().text("Allow")').click()
                except:
                    self.driver.find_element_by_android_uiautomator('new UiSelector().text("ALLOW")').click()

                self.driver.switch_to.context('WEBVIEW_com.tendercuts.app')
                time.sleep(6)
            except:
                print('location already enable')
                time.sleep(2)
            bar=self.driver.find_element_by_css_selector('#search-bar')         
            self.driver.find_element_by_css_selector('#search-bar').click()
            address_bar=self.driver.find_element_by_css_selector('input.searchbar-input')
            address_bar.clear()
            self.driver.find_element_by_css_selector('.searchbar-input').send_keys('adayar')
            time.sleep(0.8)
            option = self.driver.find_element_by_css_selector('#search-option-item-1')
            action = TouchActions(self.driver)
            action.tap(option).perform()
            time.sleep(0.4)
            update=self.driver.find_element_by_css_selector('#save-address-button')
            action = TouchActions(self.driver)
            action.tap(update).perform()
            time.sleep(4)
            outside_region=self.driver.find_element_by_css_selector(self.CSS_OUTSIDE_DELIVERY_REGION)
            action = TouchActions(self.driver)
            action.tap(outside_region).perform()


    def closer_to_another_store(self):
        time.sleep(0.8)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_ALERTTOANOTHERSTORE)))
        self.driver.find_element_by_css_selector(self.CSS_ALERTTOANOTHERSTORE).click()