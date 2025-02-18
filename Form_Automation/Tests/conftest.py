import pytest
import time
from Utils.driver import get_driver
from Utils.urlconfig import URLConfig
from Utils.locators import LoginPageElements
from Utils.locators import FormPageElements
from Pages.frompage import FormPage
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
def form_page(setup):
    form_page = FormPage(driver)
    form_page.open_page(URLConfig.LOGIN_PAGE_URL)
    return form_page