import pytest
import time
import pyperclip
from Utils.driver import get_driver
from Utils.urlconfig import URLConfig
from Utils.locators import LoginPageElements
from Pages.loginpage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.fixture(params=["chrome"])
def browser(request):
    return request.param

@pytest.fixture
def setup(browser):
    global driver
    driver = get_driver(browser)
    yield driver
    time.sleep(3)
    driver.close()

@pytest.fixture
def login_page(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    return login_page

@pytest.fixture
def copy_text(setup):
   def _copy_text(input_element):
    action = ActionChains(setup)
    action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform() 
    action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform() 
    return pyperclip.paste()  
   return _copy_text