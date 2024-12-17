from selenium.webdriver.common.by import By
from Base.seleniumdriver import SeleniumMethods
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class LoginPage(SeleniumMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username = "//input[@id='user-name']"
    _password = "//input[@id='password']"
    _login_btn = "//input[@id='login-button']"
    _shoppingcart = "//a[@class='shopping_cart_link']"


    # def getUsername(self):
    #     return self.driver.find_element("xpath", self._username)
    # def enterUsername(self, username):
    #     # self.waitForElement(self._username, locatorType="xpath",timeout=5,pollFrequency=0.5)
    #     self.getUsername().send_keys(username)

    def enterUsername(self, login):
        self.sendKeys(login, self._username, locatorType="xpath")

    # def getPassword(self):
    #     return self.driver.find_element("xpath", self._password)
    # def enterPassword(self, password):
    #     #self.getPassword().clear()
    #     self.getPassword().send_keys(password)

    def enterPassword(self, password):
        self.sendKeys(password, self._password, locatorType="xpath")

    def getClickLoginBtn(self):
        return self.driver.find_element("xpath", self._login_btn)

    def clickLoginBtn(self):
        self.getClickLoginBtn().click()

    # def clickLoginBtn(self):
    #      self.clickElement(self._login_btn, locatorType="id")

    def clearField(self, locator="", locatorType="id"):
        element = self.getElement(locator, locatorType)
        element.clear()

    def login(self, username= "", password= ""):
        self.clearField(locator=self._username,
                        locatorType="xpath")
        self.clearField(locator=self._password,
                        locatorType="xpath")
        self.enterUsername(username)
        # self.driver.implicitly_wait(2)
        self.enterPassword(password)
        self.clickLoginBtn()

    def checkLogin(self):
        loginResult = self.isElementPresent("//a[@class='shopping_cart_link']",
                                            locatorType="xpath")
        return loginResult
    def loginFailed(self):
        result = self.isElementPresent("//h3[@data-test='error']",
                                       locatorType="xpath")
        return result

    def verifiyTitle(self):
        if "Products" in self.getTitle():
            return True
        else:
            return False
