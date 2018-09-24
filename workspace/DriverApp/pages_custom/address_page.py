"""

This module to check select address functionality

"""
import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class AddressPage(lib.BasePage):
    CSS_ADDRESS_SELECT = "#deliverable-address-1"
    CSS_CHICKEN_IMAGE = "#cat-4"
   

    def __init__(self, driver):
        super().__init__(driver)

    def add_new_address(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#deliverable-address-1')))
            result = self.driver.find_element_by_id('deliverable-address-1')
            if result.is_displayed():
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#deliverable-address-1')))
                time.sleep(1)
                newaddress=self.driver.find_element_by_css_selector('#add-new-address-button')
                action = TouchActions(self.driver)
                action.tap(newaddress).perform()
                time.sleep(3)
                self.driver.switch_to.context('NATIVE_APP')
                self.driver.find_element_by_android_uiautomator('new UiSelector().text("Allow")').click()
                self.driver.switch_to.context('WEBVIEW_com.tendercuts.app')
                time.sleep(8)
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#search-bar')))
                bar=self.driver.find_element_by_css_selector('#search-bar')
                if bar.is_displayed():
                    self.driver.find_element_by_css_selector('#search-bar').click()
                    address_bar=self.driver.find_element_by_css_selector('input.searchbar-input')
                    address_bar.clear()
                    # self.driver.find_element_by_css_selector('.searchbar-clear-icon').click()
                    self.driver.find_element_by_css_selector('.searchbar-input').send_keys('Thiruninravur')
                    time.sleep(0.6)
                    option = self.driver.find_element_by_css_selector('#search-option-item-1')
                    action = TouchActions(self.driver)
                    action.tap(option).perform()
                    WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#flat-no > input')))

                    self.driver.find_element_by_css_selector('#flat-no > input').send_keys('flatno')
                    WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#street > input')))

                    self.driver.find_element_by_css_selector('#street > input').send_keys('street')
                    WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#add-new-address-submit')))

                    update=self.driver.find_element_by_css_selector('#add-new-address-submit')
                    action = TouchActions(self.driver)
                    action.tap(update).perform()
        except:
            time.sleep(3)
            self.driver.switch_to.context('NATIVE_APP')
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("Allow")').click()
            self.driver.switch_to.context('WEBVIEW_com.tendercuts.app')
            time.sleep(8)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#search-bar')))
            bar=self.driver.find_element_by_css_selector('#search-bar')
            if bar.is_displayed():
                self.driver.find_element_by_css_selector('#search-bar').click()
                address_bar=self.driver.find_element_by_css_selector('input.searchbar-input')
                address_bar.clear()
                    # self.driver.find_element_by_css_selector('.searchbar-clear-icon').click()
                self.driver.find_element_by_css_selector('.searchbar-input').send_keys('Thiruninravur')
                time.sleep(0.6)
                option = self.driver.find_element_by_css_selector('#search-option-item-1')
                action = TouchActions(self.driver)
                action.tap(option).perform()
                time.sleep(0.5)
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#flat-no > input')))
                self.driver.find_element_by_css_selector('#flat-no > input').send_keys('flatno')
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#street > input')))

                self.driver.find_element_by_css_selector('#street > input').send_keys('street')
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#add-new-address-submit')))
                time.sleep(0.5)
                update=self.driver.find_element_by_css_selector('#add-new-address-submit')
                action = TouchActions(self.driver)
                action.tap(update).perform()

    def select_existing_address(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#deliverable-address-1')))
            result = self.driver.find_element_by_id('deliverable-address-1')
            if result.is_displayed():
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#deliverable-address-1')))
                time.sleep(1)
                address=self.driver.find_element_by_css_selector(self.CSS_ADDRESS_SELECT)
                action = TouchActions(self.driver)
                action.tap(address).perform()
        except:
            time.sleep(1)
            self.driver.switch_to.context('NATIVE_APP')
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("Allow")').click()
            self.driver.switch_to.context('WEBVIEW_com.tendercuts.app')
            time.sleep(8)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#search-bar')))
            bar=self.driver.find_element_by_css_selector('#search-bar')
            if bar.is_displayed():
                self.driver.find_element_by_css_selector('#search-bar').click()
                address_bar=self.driver.find_element_by_css_selector('input.searchbar-input')
                address_bar.clear()
                    # self.driver.find_element_by_css_selector('.searchbar-clear-icon').click()
                self.driver.find_element_by_css_selector('.searchbar-input').send_keys('Tambaram')
                time.sleep(0.6)
                option = self.driver.find_element_by_css_selector('#search-option-item-1')
                action = TouchActions(self.driver)
                action.tap(option).perform()
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#flat-no > input')))

                self.driver.find_element_by_css_selector('#flat-no > input').send_keys('flatno')
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#street > input')))

                self.driver.find_element_by_css_selector('#street > input').send_keys('street')
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#add-new-address-submit')))

                update=self.driver.find_element_by_css_selector('#add-new-address-submit')
                action = TouchActions(self.driver)
                action.tap(update).perform()
        

    def verify_categorypage(self):
        """
        verify chicken image display

        """
        WebDriverWait(self.driver, 25).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'ion-spinner.spinner')))
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_css_selector(self.CSS_CHICKEN_IMAGE).is_displayed()
        assert (True == result)

    def deny_location(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#deliverable-address-1')))

            result = self.driver.find_element_by_id('deliverable-address-1')
            if result.is_displayed():
                WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#deliverable-address-1')))
                time.sleep(1)
                newaddress=self.driver.find_element_by_css_selector('#add-new-address-button')
                action = TouchActions(self.driver)
                action.tap(newaddress).perform()
                time.sleep(3)
                self.driver.switch_to.context('NATIVE_APP')
                self.driver.find_element_by_android_uiautomator('new UiSelector().text("Deny")').click()
                time.sleep(0.7)
                self.driver.find_element_by_android_uiautomator('new UiSelector().text("Deny")').click()
                self.driver.switch_to.context('WEBVIEW_com.tendercuts.app')
                time.sleep(8)

                WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.map-error')))
                map_error=self.driver.find_element_by_css_selector('.map-error').is_displayed()
                assert(map_error == True)
                bar=self.driver.find_element_by_css_selector('#search-bar')
                if bar.is_displayed():
                    self.driver.find_element_by_css_selector('#search-bar').click()
                    address_bar=self.driver.find_element_by_css_selector('input.searchbar-input')
                    address_bar.clear()
                    # self.driver.find_element_by_css_selector('.searchbar-clear-icon').click()
                    self.driver.find_element_by_css_selector('.searchbar-input').send_keys('Tambaram')
                    time.sleep(0.7)
                    option = self.driver.find_element_by_css_selector('#search-option-item-1')
                    action = TouchActions(self.driver)
                    action.tap(option).perform()
                    WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#flat-no > input')))

                    self.driver.find_element_by_css_selector('#flat-no > input').send_keys('flatno')
                    WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#street > input')))

                    self.driver.find_element_by_css_selector('#street > input').send_keys('street')
                    WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#add-new-address-submit')))
                    time.sleep(0.3)
                    update=self.driver.find_element_by_css_selector('#add-new-address-submit')
                    action = TouchActions(self.driver)
                    action.tap(update).perform()
        except:
            time.sleep(3)
            self.driver.switch_to.context('NATIVE_APP')
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("Deny")').click()
            time.sleep(0.7)
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("Deny")').click()
            self.driver.switch_to.context('WEBVIEW_com.tendercuts.app')
            time.sleep(8)

            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.map-error')))
            map_error=self.driver.find_element_by_css_selector('.map-error').is_displayed()
            assert(map_error == True)
            bar=self.driver.find_element_by_css_selector('#search-bar')
            if bar.is_displayed():
                self.driver.find_element_by_css_selector('#search-bar').click()
                address_bar=self.driver.find_element_by_css_selector('input.searchbar-input')
                address_bar.clear()
                    # self.driver.find_element_by_css_selector('.searchbar-clear-icon').click()
                self.driver.find_element_by_css_selector('.searchbar-input').send_keys('Tambaram')
                time.sleep(0.7)
                option = self.driver.find_element_by_css_selector('#search-option-item-1')
                action = TouchActions(self.driver)
                action.tap(option).perform()
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#flat-no > input')))

                self.driver.find_element_by_css_selector('#flat-no > input').send_keys('flatno')
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#street > input')))

                self.driver.find_element_by_css_selector('#street > input').send_keys('street')
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#add-new-address-submit')))
                time.sleep(0.3)
                update=self.driver.find_element_by_css_selector('#add-new-address-submit')
                action = TouchActions(self.driver)
                action.tap(update).perform()