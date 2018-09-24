
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import lib


class Humbergermenu(lib.BasePage):
    CSS_MENU = ".menubutton"
    CSS_HOME = "ios-home-outline"
    CSS_LOCATION="ios-pin-outline"
    CSS_FAQ ="ios-help-circle-outline"
    CSS_CONTACTUS="ios-call-outline"
    CSS_REFER_FRIEND="ios-people-outline"
    CSS_LOGOUT="ios-log-out-outline"
    CSS_GET_LOCATION ="#store-code"
    def __init__(self, driver):
        super().__init__(driver)

    def menu(self):

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CSS_MENU)))
        self.driver.find_element_by_css_selector(self.CSS_MENU).click()

    def home(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, self.CSS_HOME)))
        result=self.driver.find_element_by_name(self.CSS_HOME).is_displayed()
    

    def location(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, self.CSS_LOCATION)))
        result=self.driver.find_element_by_name(self.CSS_LOCATION).is_displayed()
       

    def faq(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, self.CSS_FAQ)))
        result=self.driver.find_element_by_name(self.CSS_FAQ).is_displayed()
        

    def contactus(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, self.CSS_CONTACTUS)))
        result=self.driver.find_element_by_name(self.CSS_CONTACTUS).is_displayed()
      

    def referafriend(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, self.CSS_REFER_FRIEND)))
        result=self.driver.find_element_by_name(self.CSS_REFER_FRIEND).is_displayed()
        

    def logout(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, self.CSS_LOGOUT)))
        result=self.driver.find_element_by_name(self.CSS_LOGOUT).is_displayed()
        
    def click_location(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, self.CSS_LOCATION)))
        self.driver.find_element_by_name(self.CSS_LOCATION).click()

    def get_location_name(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, self.CSS_LOCATION)))
        name=self.driver.find_element_by_css_selector(self.CSS_GET_LOCATION).text
        assert (name == 'ADAYAR')