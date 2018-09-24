"""
this module to verify homepage
"""
import time

from selenium.webdriver.common.touch_actions import TouchActions

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Homepage(lib.BasePage):
    CSS_CHICKEN_IMAGE = "#cat-4"
    CSS_TITLE = "#next-category-button"
    CSS_EMERGENCY="button.got-it-btn"

    def __init__(self, driver):
        super().__init__(driver)

    def click_categorychicken(self):
        """
        click chicken image
        """
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.CSS_EMERGENCY )))
        self.driver.find_element_by_css_selector(self.CSS_EMERGENCY).click()
        time.sleep(0.6)
        Chickenimage = self.driver.find_element_by_css_selector(self.CSS_CHICKEN_IMAGE)
        action = TouchActions(self.driver)
        action.tap(Chickenimage).perform()

    def verify_tcutspage(self):
        """
        verify title displays in category page
        """
        time.sleep(2)
        self.driver.implicitly_wait(7)
        result = self.driver.find_element_by_css_selector(self.CSS_TITLE).is_displayed()
        assert (True == result)
