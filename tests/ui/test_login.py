"""
Login test suite.
Covers valid login, invalid credentials, locked-out user, and empty-field
validation. Data is loaded from data/login_data.json for a data-driven
approach instead of hardcoding each case.
"""

import json
import os

import pytest

from config import config
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.logger import get_logger

logger = get_logger(__name__)

DATA_FILE = os.path.join(config.DATA_DIR, "login_data.json")


def load_login_cases():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


LOGIN_CASES = load_login_cases()


@pytest.mark.parametrize(
    "case",
    LOGIN_CASES,
    ids=[case["case_name"] for case in LOGIN_CASES],
)
def test_login_scenarios(driver, case):
    """
    Data-driven login test. Each row in login_data.json becomes
    one parametrized test run.
    """
    logger.info(f"Running login case: {case['case_name']}")

    login_page = LoginPage(driver).load()
    login_page.login(case["username"], case["password"])

    if case["expect_success"]:
        product_page = ProductPage(driver)
        assert product_page.is_loaded(), (
            f"Expected successful login for case '{case['case_name']}', "
            f"but inventory page did not load."
        )
    else:
        assert login_page.is_error_displayed(), (
            f"Expected an error message for case '{case['case_name']}', "
            f"but none was displayed."
        )


def test_login_error_message_text(driver):
    """Verifies the exact error message text for invalid credentials."""
    login_page = LoginPage(driver).load()
    login_page.login(config.INVALID_USERNAME, config.INVALID_PASSWORD)

    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text, (
        f"Unexpected error message: {error_text}"
    )
