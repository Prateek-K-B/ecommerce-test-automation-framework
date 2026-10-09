"""
Helper to capture and save screenshots, primarily used
for on-failure evidence capture in conftest.py.
"""

import os
from datetime import datetime

from config import config
from utils.logger import get_logger

logger = get_logger(__name__)


def capture_screenshot(driver, test_name: str) -> str:
    """
    Saves a screenshot named with the test name and timestamp.
    Returns the file path so it can be attached to reports/logs.
    """
    os.makedirs(config.SCREENSHOT_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = test_name.replace("/", "_").replace("::", "_")
    file_path = os.path.join(config.SCREENSHOT_DIR, f"{safe_name}_{timestamp}.png")

    try:
        driver.save_screenshot(file_path)
        logger.info(f"Screenshot saved: {file_path}")
    except Exception as e:
        logger.error(f"Failed to capture screenshot: {e}")
        return ""

    return file_path
