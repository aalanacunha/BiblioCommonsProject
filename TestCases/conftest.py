import pytest
from selenium import webdriver
from Base.webdrivers import WebDriver

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def driverSetup(request, browser):
    webd = WebDriver(browser)
    driver = webd.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver

        # if browser == 'Chrome':
        #     baseURL = "https://www.saucedemo.com/"
        #     driver = webdriver.Chrome()
        #     driver.get(baseURL)
        #     print("Running tests on chrome")
        # else:
        #     baseURL = "https://www.saucedemo.com/"
        #     driver = webdriver.Firefox()
        #     driver.maximize_window()
        #     driver.implicitly_wait(3)
        #     driver.get(baseURL)
        #     print("Running tests on firefox")

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
