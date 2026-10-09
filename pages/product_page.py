"""
Page Object for the SauceDemo product/inventory page.
"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def is_loaded(self) -> bool:
        return self.element_exists(self.INVENTORY_ITEM)

    def add_product_to_cart_by_name(self, product_name: str):
        """
        SauceDemo builds the 'Add to cart' button id from the product name,
        e.g. 'Sauce Labs Backpack' -> 'add-to-cart-sauce-labs-backpack'.
        """
        slug = product_name.lower().replace(" ", "-")
        button_locator = (By.ID, f"add-to-cart-{slug}")
        self.click(button_locator)

    def remove_product_from_cart_by_name(self, product_name: str):
        slug = product_name.lower().replace(" ", "-")
        button_locator = (By.ID, f"remove-{slug}")
        self.click(button_locator)

    def get_cart_count(self) -> int:
        if self.element_exists(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def get_all_product_names(self) -> list:
        elements = self.find_all(self.INVENTORY_ITEM_NAME)
        return [el.text for el in elements]
