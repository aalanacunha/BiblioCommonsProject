import os
import sys
from selenium import webdriver
import unittest
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Base import webdrivers
from pages.loginPage.login_page import LoginPage


@pytest.mark.usefixtures("driverSetup", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, driverSetup):
        self.lp = LoginPage(self.driver)

    # baseURL = "https://www.saucedemo.com/"
    # driver = webdriver.Chrome()
    # driver.get(baseURL)
    # driver.implicitly_wait(3)

    @pytest.mark.run(order=1)
    def test_userLogin(self):
        # self.driver.get(self.baseURL)
        self.lp.login("performance_glitch_user", "secret_sauce")
        result = self.lp.checkLogin()
        assert result == True
        # self.driver.quit()

    @pytest.mark.run(order=2)
    def test_invalidLogin(self):
        # self.driver.get(self.baseURL)
        self.lp.login("alana", "abcd")
        result = self.lp.loginFailed()
        assert result == True
