"""
This module to verify fresh chat tab
"""
import time

import lib


class Chatpage(lib.BasePage):
    CSS_CHATICON = "#tab-t0-3"
    CSS_CHATICON1 = "#tab-t2-3"
    UIAUTOMATOR_SENDVALUE = 'new UiSelector().text("Type a message")'
    UIAUTOMATOR_REPLY = 'new UiSelector().description("com.tendercuts.app:id/freshchat_conv_detail_send_reply_button")'
    UIAUTOMATOR_ARROWBACK = 'new UiSelector().description("Navigate up")'
    CSS_HOMEICON = "#tab-t0-0"
    CSS_HOMEICON1 = "#tab-t2-0"

    def __init__(self, driver):
        super().__init__(driver)

    def click_chatoption(self):
        """
        click chat tab

        """
        time.sleep(2)
        try:
            Chat = self.driver.find_element_by_css_selector(self.CSS_CHATICON)
            Chat.click()
        except:
            Chat = self.driver.find_element_by_css_selector(self.CSS_CHATICON1)
            Chat.click()
        self.driver.implicitly_wait(5)

    def switchcontext(self):
        """
        switch to native app

        """
        self.driver.switch_to.context('NATIVE_APP')

    def sendmsg(self):
        """
        pass value to chat[HI]

        """
        time.sleep(4)
        sendvalue = self.driver.find_element_by_android_uiautomator(self.UIAUTOMATOR_SENDVALUE)
        sendvalue.click()
        self.driver.press_keycode(36);
        self.driver.press_keycode(37);
        time.sleep(2)

    # def clicksend(self):
    #     time.sleep(2)
    #     reply = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().resourceId("com.tendercuts.app:id/freshchat_conv_detail_send_reply_button")')
    #     reply.click()

    def narrow(self):
        """
        click narrow back button

        """
        self.driver.find_element_by_android_uiautomator(self.UIAUTOMATOR_ARROWBACK).click()

    def switchtowebview(self):
        """
        change to webview
        """
        self.driver.switch_to.context('WEBVIEW_com.tendercuts.app')
        time.sleep(2)

    def clickhome(self):
        """
        click home tab
        """
        try:
            myhome = self.driver.find_element_by_css_selector(self.CSS_HOMEICON)
            myhome.click()
        except:
            myhome = self.driver.find_element_by_css_selector(self.CSS_HOMEICON1)
            myhome.click()
