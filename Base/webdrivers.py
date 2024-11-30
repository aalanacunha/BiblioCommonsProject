"""
Creates webdrivers instance based on browser configurations
"""
import traceback
from selenium import webdriver

class WebDriver():

    def __init__(self, browser):
        self.browser = browser
    """
        Set chrome driver environment based on OS
        *Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration
        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://www.saucedemo.com/"
        if self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
