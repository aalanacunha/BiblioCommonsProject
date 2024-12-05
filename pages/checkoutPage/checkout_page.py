from Base.seleniumdriver import SeleniumMethods
from pages.loginPage.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout(SeleniumMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################################
    ########### Locators ###########
    ################################

    _product1 = "//a[@id='item_4_title_link']"
    _product2 = "//div[normalize-space()='Sauce Labs Bike Light']"
    _product3 = "//div[normalize-space()='Sauce Labs Bolt T-Shirt']"
    # _add_cart_btn = "//button[@id='add-to-cart']"
    _add_cart_btn = "//button[@id='add-to-cart-sauce-labs-backpack']"
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

    # def clickproduct(self):
    #     return self.driver.find_element("xpath", self._product1)

    def selectproducts(self):
        self.clickElement(self, locator=self._product1,
                          locatorType="xpath")

    def checkProduct(self):
        result = self.isElementPresent("//span[text() = 'Products']",
                                       locatorType="xpath")
        return result

    # def addCartBtn(self):
    #     return self.driver.find_element("xpath", self._add_cart_btn)

    def clickAddCartBtn(self):
        self.clickElement(self, locator=self._add_cart_btn,
                          locatorType="xpath")


    # def shopCartIcon(self):
    #     return self.driver.find_element("xpath", self._shoppingcart)

    def clickCartIcon(self):
        self.clickElement(locator=self._shoppingcart)

    # def continueShopBtn(self):
    #     return self.driver.find_element("xpath", self._continueShop_btn)

    def clickContinueShopBtn(self):
        self.clickElement(self, locator=self._continueShop_btn,
                          locatorType="xpath")

    # def checkoutBtn(self):
    #     return self.driver.find_element("xpath", self._checkout_btn)

    def clickCheckoutBtn(self):
        self.clickElement(self, locator=self._checkout_btn,
                          locatorType="xpath")

    # def continueCheckoutBtn(self):
    #     return self.driver.find_element("xpath", self._continueCheckout_btn)

    def clickContinueCheckout(self):
        self.clickElement(self, locator=self._continueCheckout_btn,
                          locatorType="xpath")

    # def finishBtn(self):
    #     return self.driver.find_element("xpath", self._finish_btn)

    def clickfinishBtn(self):
        self.clickElement(locator=self._finish_btn)

    def checkoutmessage(self):
        return self.driver.find_element("xpath", self._checkout_message)

    # def firstName(self):
    #     return self.driver.find_element("xpath", self._firstname)

    # def enterFirstName(self):
    #     f = Faker()
    #     self._firstName().clear()
    #     self._firstName().send_keys(f.first_name())

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
