import logging

from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import Utilities.custom_logger as cl
#from python
import logging

class SeleniumMethods():

    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType)
        return False

    def isElementPresent(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            print("Not found =P")
            return False
    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element not Found: " + locator)
        return element
    def clickElement(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("element: " +locator)
        except:
            self.log.info("Cannot click on the element: " +locator)

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("cannot send data on: " +locator+ "locator type: " +locatorType)
        except:
            self.log.info("error")


    def getTitle(self):
        return self.driver.title

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            # set log.info
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            # self.log.info("Element appeared on the web page")
            print("Element appeared on the web page")
        except:
            # self.log.info("Element not appeared on the web page")
            print("Element not appeared on the web page")
        return element

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

        def clearField(self, locator="", locatorType="id"):
            """
            Clear an element field
            """
            element = self.getElement(locator, locatorType)
            element.clear()
