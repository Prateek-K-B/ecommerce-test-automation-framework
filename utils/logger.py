"""
Centralized logger used across pages, tests, and utils.
Writes to both console and a rotating log file under /logs.
"""

import logging
import os
from datetime import datetime

from config import config


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance.
    Each test run creates one log file named with the current date,
    so all logs for a day are grouped together.
    """
    os.makedirs(config.LOG_DIR, exist_ok=True)

    logger = logging.getLogger(name)

    # Avoid attaching duplicate handlers if logger is requested multiple times
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    log_file = os.path.join(
        config.LOG_DIR, f"test_run_{datetime.now().strftime('%Y-%m-%d')}.log"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
