"""
Page Object for the SauceDemo cart page.
"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def get_cart_item_count(self) -> int:
        return len(self.driver.find_elements(*self.CART_ITEM))

    def get_cart_item_names(self) -> list:
        elements = self.find_all(self.CART_ITEM_NAME)
        return [el.text for el in elements]

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
