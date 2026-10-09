"""
Cart test suite: add product, remove product, verify cart quantity badge.
Uses product_data.csv to run the same add-to-cart test across multiple
products (data-driven testing).
"""

import csv
import os

import pytest

from config import config
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.logger import get_logger

logger = get_logger(__name__)

DATA_FILE = os.path.join(config.DATA_DIR, "product_data.csv")


def load_product_names():
    with open(DATA_FILE, newline="") as f:
        reader = csv.DictReader(f)
        return [row["product_name"] for row in reader]


PRODUCT_NAMES = load_product_names()


@pytest.fixture
def logged_in_product_page(driver):
    """Reusable setup: logs in and returns the loaded product page."""
    login_page = LoginPage(driver).load()
    login_page.login(config.VALID_USERNAME, config.VALID_PASSWORD)
    product_page = ProductPage(driver)
    assert product_page.is_loaded(), "Login failed during cart test setup."
    return product_page


@pytest.mark.parametrize("product_name", PRODUCT_NAMES)
def test_add_product_to_cart(logged_in_product_page, product_name):
    logged_in_product_page.add_product_to_cart_by_name(product_name)
    assert logged_in_product_page.get_cart_count() == 1, (
        f"Cart badge did not update after adding '{product_name}'."
    )


def test_remove_product_from_cart(logged_in_product_page):
    product_name = PRODUCT_NAMES[0]
    logged_in_product_page.add_product_to_cart_by_name(product_name)
    assert logged_in_product_page.get_cart_count() == 1

    logged_in_product_page.remove_product_from_cart_by_name(product_name)
    assert logged_in_product_page.get_cart_count() == 0, (
        "Cart badge should disappear/reset after removing the only item."
    )


def test_cart_quantity_after_multiple_additions(logged_in_product_page):
    for product_name in PRODUCT_NAMES:
        logged_in_product_page.add_product_to_cart_by_name(product_name)

    assert logged_in_product_page.get_cart_count() == len(PRODUCT_NAMES), (
        "Cart count does not match number of products added."
    )


def test_cart_page_reflects_added_items(driver, logged_in_product_page):
    product_name = PRODUCT_NAMES[0]
    logged_in_product_page.add_product_to_cart_by_name(product_name)
    logged_in_product_page.go_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_cart_item_count() == 1
    assert product_name in cart_page.get_cart_item_names()
