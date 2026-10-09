"""
Creates and configures the Selenium WebDriver instance.

Uses Selenium Manager (built into Selenium 4.6+, and stable from 4.21+)
instead of a third-party driver manager. Selenium Manager resolves and
downloads the correct browser driver automatically and returns the actual
executable — avoiding the Windows "WinError 193: %1 is not a valid Win32
application" issue that can occur when a third-party manager resolves the
wrong asset (e.g. a NOTICES file instead of chromedriver.exe).

No manual driver download or PATH configuration is required on any OS.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config import config
from utils.logger import get_logger

logger = get_logger(__name__)


def get_driver():
    """
    Builds a WebDriver instance based on config.BROWSER and config.HEADLESS.
    Supports Chrome and Firefox. Driver binaries are located and managed
    automatically by Selenium Manager — no service/executable path is passed.
    """
    browser = config.BROWSER.lower()
    logger.info(f"Initializing '{browser}' driver | headless={config.HEADLESS}")

    if browser == "chrome":
        options = ChromeOptions()
        if config.HEADLESS:
            options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if config.HEADLESS:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(config.IMPLICIT_WAIT)
    return driver
