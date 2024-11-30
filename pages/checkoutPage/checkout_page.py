import faker
from faker import Faker


class Checkout():
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################################
    ########### Locators ###########
    ################################

    _product1 = "//div[normalize-space()='Sauce Labs Backpack']"
    _product2 = "//div[normalize-space()='Sauce Labs Bike Light']"
    _product3 = "//div[normalize-space()='Sauce Labs Bolt T-Shirt']"
    _add_cart_btn = "//button[@id='add-to-cart']"
    _remove_btn = "//button[@id='remove']"  # checkifElement is present
    _back_btn = "//button[@id='back-to-products']"
    _shoppingcart = "//a[@class='shopping_cart_link']"  # check if link is there and click
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

    def clickproduct(self):
        return self.driver.find_element("xpath", self._product1)

    def selectproducts(self, _product1):
        self.clickProduct().click()

    def checkProduct(self):
        result = self.isElementPresent("//span[text() = 'Products']", LocatorType="xpath")
        return result

    def addCartBtn(self):
        return self.driver.find_element("xpath", self._add_cart_btn)

    def clickAddCartBtn(self):
        self.clickCartBtn().click()

    def shopCartIcon(self):
        return self.driver.find_element("xpath", self._shoppingcart)

    def clickCartIcon(self):
        self.shopCartIcon().click()

    def continueShopBtn(self):
        return self.driver.find_element("xpath", self._continueShop_btn)

    def clickContinueShopBtn(self):
        self.continueShopBtn().click()

    def checkoutBtn(self):
        return self.driver.find_element("xpath", self._checkout_btn)

    def clickCheckoutBtn(self):
        self.checkoutBtn().click()

    def continueCheckoutBtn(self):
        return self.driver.find_element("xpath", self._continueCheckout_btn)

    def clickContinueCheckout(self):
        self.continueCheckoutBtn().click()

    def finishBtn(self):
        return self.driver.find_element("xpath", self._finish_btn)

    def clickfinishBtn(self):
        self.finishBtn().click()

    def checkoutmessage(self):
        return self.driver.find_element("xpath", self._checkout_message)

    def firstName(self):
        return self.driver.find_element("xpath", self._firstname)

    def enterFirstName(self):
        f = Faker()
        self.firstName().clear()
        self.firstName().send_keys(f.first_name())

    def lastName(self):
        return self.driver.find_element("xpath", self._lastname)

    def enterLastName(self):
        f = Faker()
        self.lasName.clear()
        self.lastName().send_keys(f.last_name())

    def zipcode(self):
        return self.driver.find_element("xpath", self._zipcode)

    def enterZipcode(self):
        f = Faker()
        self.zipcode().clear()
        self.zipcode().send_keys(f.zipcode())

    def enterInformation(self, _firstname, _lastname, _zipcode):
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
