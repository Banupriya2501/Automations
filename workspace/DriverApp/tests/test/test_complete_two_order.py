import pages
import time
import datetime
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import lib
import pytest
from appium import webdriver
import MySQLdb
import datetime

import time
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('test_checkout_two_order.feature', 'assign two order and complete it')
def test_Assign_two_order():
    """PlacingOrder_cod."""
    pass

@given('a username <username> and <password> click submit button')
def a_username_username_and_password_click_submit_button(driver,username,password):
    """a username <username> and <password> click submit button."""
    loginpage=pages.Loginpage(driver)
    loginpage.enter_username(username=username)
    loginpage.enter_password(password=password)
    loginpage.submit()

@when('click store')
def click_store(driver):
    storepicker=pages.Storepickerpage(driver)
    storepicker.click_store()

@then('click online')
def click_online(driver):
    orderpage=pages.Orderpage(driver)
    orderpage.click_online()

@then('enter orderid and search')
def enter_orderid_and_search(driver):
    time.sleep(3)
    db= MySQLdb.connect(host="139.162.51.169", user="root", passwd="!qazmlp)5", db="v3_5", port=3306)
    cur = db.cursor()
    i=0
    while i < 2 :
        orderid="""SELECT a.increment_id FROM sales_flat_order AS a join sales_flat_order_address AS b ON a.entity_id = b.parent_id WHERE b.telephone = '9710243651' AND a.status = 'pending' ORDER BY increment_id DESC LIMIT 1"""
        cur.execute(orderid)
        rows = cur.fetchall()
        for row in rows:
            print(row[0])
        order=row[0]
        move_proccessing="""UPDATE sales_flat_order SET status = 'processing' WHERE increment_id = {}""".format(order)
        move_proccessing1="""UPDATE sales_flat_order_grid SET status = 'processing' WHERE increment_id = {}""".format(order)
        cur.execute(move_proccessing)
        cur.execute(move_proccessing1)
        db.commit()
        orderpicker=pages.Orderpickerpage(driver)
        time.sleep(1)
        orderpicker.enter_orderid(order)
        time.sleep(1)
        orderpicker.click_search()
        time.sleep(1)
        import pdb
        pdb.set_trace()
        orderpicker.assignorder()
        orderpicker.alert()
        time.sleep(1)
        orderpicker.barcode()
        time.sleep(1)
        orderpicker.done()
        time.sleep(1)
        orderpicker.assign()
        time.sleep(1)
        i=i+1

@then('donebutton')
def done(driver):
    time.sleep(1)
    orderpicker=pages.Orderpickerpage(driver)
    orderpicker.donebutton()

@then('complete the order')
def complete(driver):
    orderpicker=pages.Orderpickerpage(driver)
    orderpicker.completeorder()
    orderpicker.complete_the_order()
    orderpicker.alert()

@then('click complete later')
def complete_later(driver):
    import pdb
    pdb.set_trace()
    orderpicker=pages.Orderpickerpage(driver)
    orderpicker.complete_later()
    orderpicker.alert()


@then('assign order and complete the order')
def assign_order(driver):
    import pdb
    pdb.set_trace()
    i=0
    while i < 2:
        orderpicker=pages.Orderpickerpage(driver)
        orderpicker.completeorder()
        orderpicker.complete_the_order()
        orderpicker.alert()
        i=i+1
        time.sleep(1)



# @then('enter orderid and search<orderid>')
# def enter_orderid_and_search(driver,orderid):
#     time.sleep(3)
#     orderpicker=pages.Orderpickerpage(driver)
#     orderpicker.enter_orderid(orderid)
#     orderpicker.click_search()


# @then('assign the order')
# def assign_the_order(driver):
#     orderpicker=pages.Orderpickerpage(driver)
#     orderpicker.assignorder()
#     orderpicker.alert()

# @then('enter the barcode and assignorder')
# def barcode(driver):
#     orderpicker=pages.Orderpickerpage(driver)
#     orderpicker.barcode()
#     orderpicker.done()
#     orderpicker.assign()

# @then('enter the barcode and assign order')
# def barcode(driver):
#     orderpicker=pages.Orderpickerpage(driver)
#     orderpicker.barcode()
#     orderpicker.done()
#     orderpicker.assign()
#     orderpicker.donebutton()

# @then('assign another order')
# def assign_the_order(driver):
#     orderpicker=pages.Orderpickerpage(driver)
#     orderpicker.assignorder()
#     orderpicker.alert()


 
