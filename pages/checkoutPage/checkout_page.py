from Base.seleniumdriver import SeleniumMethods
from selenium import webdriver
from pages.loginPage.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Checkout(SeleniumMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################################
    ########### Locators ###########
    ################################

    _product1 = "(//div[normalize-space()='Sauce Labs Backpack'])[1]"
    _product2 = "//div[normalize-space()='Sauce Labs Bike Light']"
    _product3 = "//div[normalize-space()='Sauce Labs Bolt T-Shirt']"
    # _add_cart_btn = "//button[@id='add-to-cart']"
    _add_cart_btn = "//button[@id='add-to-cart']"
    # _add_cart_btn = "//button[@id='add-to-cart-sauce-labs-backpack']"
    _remove_btn = "//button[@id='remove']"
    _back_btn = "//button[@id='back-to-products']"
    _shoppingcart = "//a[@class='shopping_cart_link']"
    _continueShop_btn = "//button[@id='continue-shopping']"
    _checkout_btn = "//button[@id='checkout']"
    _continueCheckout_btn = "//input[@id='continue']"
    _finish_btn = "//button[@id='finish']"
    _checkout_message = "//h2[contains(.,'Thank you for your order!')]"
    # fakedata here
    _firstname = "//input[@id='first-name']"  # click first and type
    _lastname = "//input[@id='last-name']"
    _zipcode = "//input[@id='postal-code']"

    ############################
    ### Element Interactions ###
    ############################

    def clickproduct(self, locatorType="xpath"):
        try:
            element = self.getElement(self._product1, "xpath")
            element.click()
        except:
            print("Cannot click on the element: ")

    # def clickproduct(self):
    #     WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(By.XPATH, self._product1))
    #     return self.driver.find_element(By.XPATH, self._product1)
    #
    # def selectproducts(self):
    #     self.clickproduct().click()
    #     print("pass")

    def checkProduct(self):
        result = self.isElementPresent("//span[text() = 'Products']",
                                       locatorType="xpath")
        return result

    # def addCartBtn(self):
    #     return self.driver.find_element("xpath", self._add_cart_btn)

    def clickAddCartBtn(self, locatorType="xpath"):
        try:
            element = self.getElement(self._add_cart_btn, "xpath")
            element.click()
        except:
            print("Cannot click on the element: ")



    # def shopCartIcon(self):
    #     return self.driver.find_element("xpath", self._shoppingcart)

    def clickCartIcon(self, locatorType="xpath"):
        try:
            element = self.getElement(self._shoppingcart, "xpath")
            element.click()
        except:
            print("Cannot click on the element: ")

    # def continueShopBtn(self):
    #     return self.driver.find_element("xpath", self._continueShop_btn)

    def clickContinueShopBtn(self):
        try:
            element = self.getElement(self._continueShop_btn, "xpath")
            element.click()
        except:
            print("Cannot click on the element: ")

    # def checkoutBtn(self):
    #     return self.driver.find_element("xpath", self._checkout_btn)

    def clickCheckoutBtn(self):
        # self.clickElement(self, locator=self._checkout_btn,
        #                   locatorType="xpath")
        try:
            element = self.getElement(self._checkout_btn, "xpath")
            element.click()
        except:
            print("Cannot click on the element: ")

    # def continueCheckoutBtn(self):
    #     return self.driver.find_element("xpath", self._continueCheckout_btn)

    def clickContinueCheckout(self):
        # self.clickElement(self, locator=self._continueCheckout_btn,
        #                   locatorType="xpath")
        try:
            element = self.getElement(self._continueCheckout_btn, "xpath")
            element.click()
        except:
            print("Cannot click on the element: ")

    # def finishBtn(self):
    #     return self.driver.find_element("xpath", self._finish_btn)

    def clickfinishBtn(self):
        try:
            element = self.getElement(self._finish_btn, "xpath")
            element.click()
        except:
            print("Cannot click on the element: ")

    def checkoutmessage(self):
        return self.driver.find_element("xpath", self._checkout_message)


    def enterFirstName(self, first_name):
        self.sendKeys(first_name, self._firstname,
                      locatorType="xpath")

    # def lastName(self):
    #     return self.driver.find_element("xpath", self._lastname)

    def enterLastName(self, last_name):
        self.sendKeys(last_name, self._lastname,
                      locatorType="xpath")

    # def zipcode(self):
    #     return self.driver.find_element("xpath", self._zipcode)

    def enterZipcode(self, zipcode):
        self.sendKeys(zipcode, self._zipcode,
                      locatorType="xpath")

    def enterInformation(self, first_name, last_name, zipcode):
        self.enterFirstName()
        self.enterLastName()
        self.enterZipcode()

    def checkoutForm(self):
        # self.webScroll(direction = "down")
        self.enterInformation()
        self.clickContinueCheckout()
    def verifyCheckout(self):
        message = self.waitForElement(self._checkout_message)
        self.checkProduct()
        self.clickfinishBtn()
        result = self.isElementDisplayed(element=message)
        return result
