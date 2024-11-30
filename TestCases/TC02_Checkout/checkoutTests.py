from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.checkoutPage.checkout_page import Checkout
from pages.loginPage.login_page import LoginPage
import unittest
import pytest
from faker import Faker

pytest.mark.usefixtures("driverSetup", "setUp")


class CheckoutTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, driverSetup):
        self.lp = LoginPage(self)
        self.cp = Checkout(self)

    @pytest.mark.run(order=1)
    def test_selectProduct(self):
        self.cp.selectproducts()
        result = self.cp.checkProduct()
        result == True

    def test_addingProductsCart(self):
        self.cp.clickAddCartBtn()
        self.cp.clickCartIcon()
        result = self.cp.checkProduct()
        result == True
        self.cp.continueShopBtn()

    def test_checkoutProducts(self):
        self.cp.clickCartIcon()
        result = self.cp.checkProduct()
        result == True
        self.cp.clickCheckoutBtn()
        self.cp.checkoutForm()
        result = self.cp.checkoutmessage()
        assert result == True

