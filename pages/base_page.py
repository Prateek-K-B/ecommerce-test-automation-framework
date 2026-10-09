"""
BasePage centralizes common Selenium actions (find, click, type, wait)
so every page class inherits consistent, reusable behavior instead of
duplicating raw Selenium calls everywhere.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT_TIMEOUT)

    def open(self, url: str):
        logger.info(f"Navigating to {url}")
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        return self.find(locator).text

    def is_visible(self, locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def element_exists(self, locator) -> bool:
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0
