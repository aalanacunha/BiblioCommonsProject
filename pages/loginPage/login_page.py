from selenium.webdriver.common.by import By
from Base.seleniumdriver import SeleniumMethods


class LoginPage():

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username = "//input[@id='password']"
    _password = "//input[@id='password']"
    _login_btn = "login-button"

    def getUsername(self):
        return self.driver.find_element("xpath", self._username)
    def enterUsername(self, username):
        self.getUsername().clear()
        self.getUsername().send_keys(username)
    def getPassword(self):
        return self.driver.find_element("xpath", self._password)
    def enterPassword(self, password):
        self.getPassword().clear()
        self.getPassword().send_keys(password)
    def getClickLoginBtn(self):
        return self.driver.find_element("xpath", self._login_btn)
    def clickLoginBtn(self, login_btn):
        self.getClickLoginBtn().click()

    def login(self, username, password):
        self.enterUsername()
        self.enterPassword()
        self.clickLoginBtn()

    def checkLogin(self):
        loginResult = self.isElementPresent("//span[text() = 'Products']", LocatorType="xpath")
        return loginResult
    def loginFailed(self):
        result = self.isElementPresent("//h3[@data-test='error']", locatorType="xpath")
        return result


    # def verifiyTitle(self):
    #     if "title" self.getTitle():
    #         return True
    #     else:
    #         return False
