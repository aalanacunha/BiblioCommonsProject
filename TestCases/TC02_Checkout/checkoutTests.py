from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.checkoutPage.checkout_page import Checkout
import unittest
import pytest
from faker import Faker


class CheckoutTests(unittest.TestCase):
    url = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(3)
    # lp = LoginPage(driver)
    cp = Checkout(driver)


    def test_addingProducts_to_cart(self):
        self.driver.get(self.url)
        self.cp.add_product_verify_cart()
        result = self.cp.add_product_verify_cart()
        assert result == True
        self.cp.return_products_page()

    def test_checkoutProducts(self):
        f = Faker(["en_EN"])
        #click on checkout button


        self.f.first_name()
        f.last_name()
        f.zipcode()


