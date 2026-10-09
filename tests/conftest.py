"""
Shared PyTest fixtures and hooks.

- `driver` fixture: creates a fresh browser session per UI test and quits it after.
- `pytest_runtest_makereport` hook: automatically captures a screenshot
  whenever a UI test fails, and saves it under /screenshots.
"""

import pytest

from utils.driver_factory import get_driver
from utils.screenshot_helper import capture_screenshot
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.fixture
def driver():
    """Provides a fresh WebDriver instance for each UI test, then tears it down."""
    logger.info("---- Starting new browser session ----")
    driver_instance = get_driver()
    yield driver_instance
    logger.info("---- Closing browser session ----")
    driver_instance.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Hook that runs after each test phase (setup/call/teardown).
    If the 'call' phase failed and the test used the `driver` fixture,
    a screenshot is captured for debugging.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("driver")
        if driver_instance is not None:
            screenshot_path = capture_screenshot(driver_instance, item.name)
            if screenshot_path:
                logger.error(f"Test failed: {item.name}. Screenshot: {screenshot_path}")
