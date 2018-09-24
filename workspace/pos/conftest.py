import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="function",autouse=True)
def driver(request):

    driver = webdriver.Chrome()
    driver.get("https://staging.tendercuts.in/v3/website/tpos/webpos")
    
    def kill_app():
        driver.quit()

    request.addfinalizer(kill_app)
    return driver


# cap = DesiredCapabilities().FIREFOX
#     cap["marionette"] = False
#     driver = webdriver.Firefox(capabilities=cap, executable_path="\\usr\\local\\bin\\geckodriver.exe")
#     driver.get("https://staging.tendercuts.in/v3/website/tpos/webpos")
    
