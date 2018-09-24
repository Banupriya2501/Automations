
"""

This module to check signin functionality

"""
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lib


class Purchasepage(lib.BasePage):

    XPATH_HUMBERGER_MENU = "//nav[2]/div/div/a/i"
    XPATH_PURCHASEAPP = "//img[@alt='Purchases']"
    XPATH_CREATE="(//button[@type='button'])[7]"
    XPATH_VENDORSELECTION="//input[@class='o_input ui-autocomplete-input']"
    CSSSELECTOR_LIST_VENDOR=".ui-menu-item.ui-state-focus > a"
    NAME_COMPANY="company_id"
    LINK_COMPANY="Adayar"
    LINK_ADDITEM="Add an item"
    # XPATH_QUANTITY=""
    # NAME_CHANGEQUANTITY=""
    # XPATH_SAVE=""
    # XPATH_CONFIRM=""
    # NAME_GETPO=""
    # XPATH_RECEIVED=""
    # NAME_VENDORBILL=""
    # XPATH_ATTACH=""
    # NAME_EDIT=""
    # XPATH_PLU=""
    # XPATH_INITIALDEMAND=""
    # NAME_PLU=""
    # ID_WEIGHT=""
    # XPATH_ENTERWEIGHT=""
    # XPATH_VALIDATE=""
    # LINK_PURCHASETAB=""
    # LINK_PURCHSEMENU
    # LINK_PO=""

    def __init__(self, driver):
        super().__init__(driver)


    def purchase_app(self):
        # time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_PURCHASEAPP)))
        self.driver.find_element_by_xpath(self.XPATH_PURCHASEAPP).click()

    def humberger_menu(self):
        # time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_HUMBERGER_MENU)))
        self.driver.find_element_by_xpath(self.XPATH_HUMBERGER_MENU).click()

    # def change_vendor(self):
    #     self.driver.implicitly_wait(13)
    #     self.driver.find_element_by_css_selector("li.o_switch_company_menu > a.dropdown-toggle > span.oe_topbar_name").click()
    #     self.driver.find_element_by_link_text("Envee - CPU").click()


    def create(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_CREATE)))
        
        time.sleep(0.5)

        self.driver.find_element_by_xpath(self.XPATH_CREATE).click()

    def vendor_selection(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_VENDORSELECTION)))
        # time.sleep(0.5)
        self.driver.find_element_by_xpath(self.XPATH_VENDORSELECTION).send_keys("Envee-test")
        # time.sleep(0.4)
        self.driver.find_element_by_css_selector(self.CSSSELECTOR_LIST_VENDOR).click()
    

    def company_selection(self):
        # time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.NAME, self.NAME_COMPANY)))
        

        self.driver.find_element_by_name(self.NAME_COMPANY).click()
        # time.sleep(0.3)
        self.driver.find_element_by_link_text(self.LINK_COMPANY).click()


    def add_item(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Add an item')))
        time.sleep(0.5)
        self.driver.find_element_by_link_text("Add an item").click()    

    def add_product(self):
  
        # product_id = ["102","103","104","105","106","107","108","109","301","570"]
        # product_name=["[RM_MRT_CHTD_CHK_65,102] Chicken 65 With Bone",
        #               "[RM_MRT_CHK_65_BL,103] Chicken 65 Boneless",
        #               "[RM_MRT_MALAI_CHK,104] Malai Chicken",
        #               "[RM_MRT_PERI PERI_CHK,105] Peri Peri Chicken",
        #               "[RM_MRT_LEMONE_CHK,106] Spicy Lemon Chicken",
        #               "[RM_MRT_SCHZN_CHK_LOLLIPOP,107] Schezwan Chicken Lollipop",
        #               "[RM_MRT_GLAZE_WINGS,108] Chicken Hot Wings",
        #               "[RM_RP_CHK_POPCORN,109] Chicken Popcorn",
        #               "[RM_MRT_RAWA_FISH,301] Karavali Rawa Fish Fry",
        #               "[RM_MRT_MELTING_TIKKA,570] Melting Keema Tikka"]
        # quantity=["5","10","15","20","25","30","35","40","45","50"]
        product_id=["1008"]
        product_name =["[ING_RM_CHK_TL_BL,1008] Chicken Tigh&Leg Boneless"]
        quantity=["5"]
        for i in range(0,1):
            Purchasepage.add_item(self)
            self.driver.find_element_by_xpath("//div[@name='product_id']//input").click()
            self.driver.find_element_by_xpath("//div[@name='product_id']//input").send_keys(product_id[i])
            time.sleep(0.3)
            WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.LINK_TEXT,''+product_name[i]+'')))

            self.driver.find_element_by_link_text(product_name[i]).click()
            time.sleep(0.3)
            Purchasepage.change_qunatity(self,quantity[i])
            time.sleep(0.5)

    def change_qunatity(self,quantity):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.NAME, 'product_qty')))
        time.sleep(0.5)
        self.driver.find_element_by_name("product_qty").click()
        self.driver.find_element_by_name("product_qty").clear()
        self.driver.find_element_by_name("product_qty").send_keys(quantity)

    def save(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH,'(//button[@type="button"])[9]')))
        self.driver.find_element_by_xpath("(//button[@type='button'])[9]").click()

    def confirmorder(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[5]')))
        
        self.driver.find_element_by_xpath("//button[5]").click()

    def get_po(self):
        time.sleep(1)
        global po
        po=self.driver.find_element_by_name("name").text

    def received_product(self):
        time.sleep(1)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[9]')))
        
        self.driver.find_element_by_xpath("//button[9]").click()

    def vendor_bill(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.NAME, 'vendor_reference')))
        
        self.driver.find_element_by_name("vendor_reference").click()
        self.driver.find_element_by_name("vendor_reference").clear()
        self.driver.find_element_by_name("vendor_reference").send_keys("123123")
        
    def update_screenshot(self):
        import pdb
        pdb.set_trace()
        print('hi')
        # self.driver.find_element_by_xpath("(//button[@type='button'])[25]").click()
        # self.driver.find_element_by_name("ufile").click()
        # self.driver.find_element_by_name("ufile").clear()
        # e= self.driver.find_element_by_xpath("//div/input[@type='text']")
        # e.send_keys("/home/banupriya/workspace/envee/picture/empty.png")
    

    def click_attach(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.NAME, 'action_attach_bill')))
        
        time.sleep(0.5)
        self.driver.find_element_by_name("action_attach_bill").click()
    

    def edit(self):
        import pdb
        pdb.set_trace()
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '(//button[@type="button"])[7]')))
        
        self.driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        time.sleep(0.5)

    def barcode_plu(self):
        import pdb
        pdb.set_trace()
        time.sleep(0.5)
        self.driver.implicitly_wait(13)
        for i in range(1,2):
            time.sleep(0.3)
            WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr['+ str(i) +']/td[6]')))

            # plu=self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr["+ str(i) +"]/td[6]").text
            # # import string
            # validchars = string.digits
            # plu1=''.join(c for c in plu if c in validchars)
            initial_demand=self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr["+ str(i) +"]/td[2]").text
            time.sleep(0.3)
            self.driver.find_element_by_name("plu_code").click()
            self.driver.find_element_by_name("plu_code").clear()
            self.driver.find_element_by_name("plu_code").send_keys("1001012018072005000")
            self.driver.find_element_by_name("plu_code").send_keys(Keys.ENTER)
            time.sleep(0.5)
            # Purchasepage.weight(self,initial_demand)
            time.sleep(0.2)
            Purchasepage.enter_weight(self)
            time.sleep(0.3)


    def weight(self,initial_demand):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.ID, 'weightField')))
        
        self.driver.find_element_by_id("weightField").clear()
        self.driver.find_element_by_id("weightField").send_keys(initial_demand)
        
    def enter_weight(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[6]/div/div/div[3]/button')))
        
        self.driver.find_element_by_xpath("html/body/div[6]/div/div/div[3]/button").click()

    def validate(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/button[3]')))
        
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/button[3]").click()
        time.sleep(1)

    def purchase_tab(self):
        time.sleep(0.8)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Purchase')))
        self.driver.find_element_by_link_text("Purchase").click()
    
    def purchase_order(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Purchase Orders')))
        self.driver.find_element_by_link_text("Purchase Orders").click()

    def click_po(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//tr[1]/td[2]')))
        po_number=self.driver.find_element_by_xpath("//tr[1]/td[2]").text
        assert (po == po_number)