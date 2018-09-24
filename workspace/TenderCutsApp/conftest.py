import pytest
from appium import webdriver
import MySQLdb
import datetime

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    desired_caps = {
        'platformName': 'Android',
        'platformVion': '6.0',
        'deviceName': 'emulator-5554',
        'isHeadless': 'true',
        # 'app'       : '/test/build/android-debug.apk',
        'fastReset': 'true',
        'appPackage': 'com.tendercuts.app',
        'appActivity': 'com.tendercuts.app.MainActivity',
        "newCommandTimeout": 60 * 5
    }
    today = format(datetime.date.today(), "%y-%m-%d")
    db= MySQLdb.connect(host="139.162.51.169", user="root", passwd="!qazmlp)5", db="v3_5", port=3306)
    cur = db.cursor()
    delete="""DELETE FROM graminventory WHERE product_id=450"""
    deletequery="""DELETE FROM graminventory WHERE product_id=193"""
    query = """INSERT INTO graminventory (date,product_id,store_id,opening,qty,expiringtoday,forecastqty) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute(deletequery)
    cur.execute(delete)
    cur.execute(query, (today,193,7,100.0000,1,00.0000,1))
    cur.execute(query, (today,450,7,100.0000,1,00.0000,1))
    db.commit()
 
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.set_location(80,12,00)
    driver.switch_to.context('WEBVIEW_com.tendercuts.app')
    def kill_app():
        driver.quit()

    request.addfinalizer(kill_app)
    return driver