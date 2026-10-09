"""
End-to-end checkout test.
Flow: Login -> Select Product -> Add to Cart -> Checkout -> Complete Order.
This is the single most important test in the suite because it validates
a full user journey rather than one isolated feature.
"""

from config import config
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.logger import get_logger

logger = get_logger(__name__)


def test_end_to_end_checkout_flow(driver):
    logger.info("Starting end-to-end checkout flow test")

    # Step 1: Login
    login_page = LoginPage(driver).load()
    login_page.login(config.VALID_USERNAME, config.VALID_PASSWORD)

    product_page = ProductPage(driver)
    assert product_page.is_loaded(), "Login failed — inventory page did not load."

    # Step 2: Select product and add to cart
    product_name = "Sauce Labs Backpack"
    product_page.add_product_to_cart_by_name(product_name)
    assert product_page.get_cart_count() == 1, "Product was not added to cart."

    # Step 3: Go to cart and proceed to checkout
    product_page.go_to_cart()
    cart_page = CartPage(driver)
    assert product_name in cart_page.get_cart_item_names()
    cart_page.proceed_to_checkout()

    # Step 4: Fill checkout information
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_information("Prateek", "Byadgi", "560001")

    # Step 5: Finish order
    checkout_page.finish_order()
    assert checkout_page.is_order_complete(), "Order completion page was not shown."

    confirmation_text = checkout_page.get_confirmation_message()
    assert "Thank you for your order" in confirmation_text, (
        f"Unexpected confirmation message: {confirmation_text}"
    )

    logger.info("End-to-end checkout flow completed successfully")


def test_checkout_blocks_without_required_fields(driver):
    """Negative case: checkout should not proceed if required fields are empty."""
    login_page = LoginPage(driver).load()
    login_page.login(config.VALID_USERNAME, config.VALID_PASSWORD)

    product_page = ProductPage(driver)
    product_name = "Sauce Labs Backpack"
    product_page.add_product_to_cart_by_name(product_name)
    product_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_information("", "", "")

    assert checkout_page.is_visible(checkout_page.ERROR_MESSAGE), (
        "Expected a validation error when required checkout fields are empty."
    )
