"""
Central configuration for the automation suite.
No secrets, no API keys, no database — everything runs locally
against public demo endpoints.
"""

# ---------- UI Testing (SauceDemo) ----------
import os
UI_BASE_URL = "https://www.saucedemo.com/"

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"

LOCKED_OUT_USERNAME = "locked_out_user"
INVALID_USERNAME = "invalid_user"
INVALID_PASSWORD = "invalid_password"

# ---------- API Testing (DummyJSON) ----------
API_BASE_URL = "https://dummyjson.com"

# ---------- Browser Settings ----------
BROWSER = "chrome"
HEADLESS = os.getenv("CI", "").lower() == "true"
IMPLICIT_WAIT = 5
EXPLICIT_WAIT_TIMEOUT = 10

# ---------- Paths ----------
SCREENSHOT_DIR = "screenshots"
REPORT_DIR = "reports"
LOG_DIR = "logs"
DATA_DIR = "data"
