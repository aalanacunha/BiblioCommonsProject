from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.checkoutPage.checkout_page import Checkout
import unittest
import pytest
from faker import Faker

@pytest.mark.usefixtures("webDriverSetup", "setUp")

class CheckoutTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, webDriverSetup):
        self.cp = Checkout(self.driver)

    @pytest.mark.run(order=1)
    def test_selectProduct(self):
        self.cp.clickproduct()
        result = self.cp.checkProduct()
        result == True

    @pytest.mark.run(order=2)
    def test_addingProductsCart(self):
        self.cp.clickAddCartBtn()
        self.cp.clickCartIcon()
        result = self.cp.checkProduct()
        result == True
        self.cp._continueShop_btn()

    @pytest.mark.run(order=3)
    def test_checkoutProducts(self):
        self.cp.clickCartIcon()
        result = self.cp.checkProduct()
        result == True
        self.cp.clickCheckoutBtn()
        # self.cp.checkoutForm()
        # result = self.cp.checkoutmessage()
        # assert result == True

    # @pytest.mark.run(order=4)
    # def test_completeCheckoutForm(self, first_name, last_name, zipcode):
    #     f = Faker()
    #     self.cp.checkoutForm(f.first_name(), f.last_name(), f.zipcode())
    #     result = self.cp.checkoutmessage()
    #     assert result == True

