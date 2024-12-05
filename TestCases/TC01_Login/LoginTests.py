import os
import sys
from selenium import webdriver
from faker import Faker
import unittest
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Base import webdrivers
from pages.loginPage.login_page import LoginPage
from pages.checkoutPage.checkout_page import Checkout

'''
py.test -s -v TestCases/TC01_Login/LoginTests.py --html=testreport.html;
'''
@pytest.mark.usefixtures("webDriverSetup", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)  #making fixture available to test all the functions without requesting
    def classSetup(self, webDriverSetup):
        self.lp = LoginPage(self.driver)
        # self.cp = Checkout(self.driver)


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("alana", "abcd")
        result = self.lp.loginFailed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_userLogin(self):
        self.lp.login("performance_glitch_user", "secret_sauce")
        # result = self.lp.getTitle()
        # assert result == True
        result2 = self.lp.checkLogin()
        assert result2 == True
