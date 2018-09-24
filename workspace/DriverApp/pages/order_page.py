import time

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import lib


class Orderpage(lib.BasePage):

    CSS_ONLINE=".go-online"
    CSS_SCAN=".header > ion-row > ion-col + ion-col > button"

    def __init__(self, driver):
        super().__init__(driver)

    def click_online(self):
        # WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_SCAN)))
        time.sleep(2)
        try:
            self.driver.find_element_by_css_selector(self.CSS_SCAN).click()

        except:
            self.driver.find_element_by_css_selector(self. CSS_ONLINE).click()
            time.sleep(1)
            self.driver.find_element_by_css_selector(self.CSS_SCAN).click()


    def verify(self):
        """
        Verify it redirect to location page

        """
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_STOREPICKER)))
        
        self.driver.find_element_by_css_selector(self.CSS_STOREPICKER).click()
