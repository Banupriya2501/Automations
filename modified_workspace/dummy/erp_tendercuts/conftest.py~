import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime

@pytest.fixture(scope="function",autouse=True)
def driver(request):

    driver = webdriver.Chrome()
    driver.get("http://localhost:8069")
    driver.maximize_window()

    def kill_app():
        driver.quit()
 
    request.addfinalizer(kill_app)
    return driver
