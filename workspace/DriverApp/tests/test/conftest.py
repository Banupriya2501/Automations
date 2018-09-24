import pytest
from appium import webdriver
import MySQLdb
import datetime
import time

@pytest.fixture(scope="function",autouse=True)
def driver(request):
    desired_caps = {
        'platformName': 'Android',
        'platformVion': '6.0',
        'deviceName': 'emulator-5554',
        'isHeadless': 'true',
        'fastReset': 'true',
        'appPackage': 'com.tendercuts.driver',
        'appActivity': 'com.tendercuts.driver.MainActivity',
        "newCommandTimeout": 60 * 5

    }
    # import pdb
    # pdb.set_trace()
    # time.sleep(3)
    # db= MySQLdb.connect(host="139.162.51.169", user="root", passwd="!qazmlp)5", db="v3_5", port=3306)
    # cur = db.cursor()
    # orderid="""SELECT a.increment_id FROM sales_flat_order AS a join sales_flat_order_address AS b ON a.entity_id = b.parent_id WHERE b.telephone = '9710243651' AND a.status = 'out_delivery' ORDER BY increment_id DESC LIMIT 2"""
    # cur.execute(orderid)
    # rows = cur.fetchall()
    # row = []
    # for row in rows:
    #     print(row[0])
    # order=row[0]
    # move_proccessing="""UPDATE sales_flat_order SET status = 'Canceled' WHERE increment_id = {}""".format(order)
    # move_proccessing1="""UPDATE sales_flat_order_grid SET status = 'canceled' WHERE increment_id = {}""".format(order)
    # cur.execute(move_proccessing)
    # cur.execute(move_proccessing1)
    # db.commit()



    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.set_location(80, 12, 00)
    driver.switch_to.context('WEBVIEW_com.tendercuts.driver')
    
    def kill_app():
        driver.quit()
        
    request.addfinalizer(kill_app)
    return driver