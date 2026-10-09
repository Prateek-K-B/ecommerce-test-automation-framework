# E-Commerce Test Automation Framework

A Python-based QA automation framework for testing an e-commerce application using Selenium WebDriver, PyTest, and Requests.

This project demonstrates practical QA automation skills including Page Object Model (POM), data-driven testing, UI automation, API testing, logging, HTML reporting, screenshot capture, and CI/CD integration.

---

## Project Overview

| Area | Technology |
|---|---|
| Programming Language | Python |
| UI Automation | Selenium WebDriver |
| Test Framework | PyTest |
| API Testing | Requests |
| Design Pattern | Page Object Model (POM) |
| Test Data | JSON / CSV |
| Reporting | pytest-html |
| Browser | Google Chrome |
| Driver Management | Selenium Manager |
| CI/CD | GitHub Actions |
| Version Control | Git / GitHub |

### Applications Tested

- **UI:** SauceDemo
- **API:** DummyJSON

---

## Test Coverage

### UI Testing

The framework covers:

- Valid login
- Invalid username
- Invalid password
- Locked-out user
- Empty username/password validation
- Add product to cart
- Remove product from cart
- Cart quantity validation
- Cart item validation
- End-to-end checkout
- Checkout required-field validation

### API Testing

The framework covers:

- GET all products
- GET single product
- Product response validation
- 404 response validation
- POST product creation
- Status code validation
- Response body validation

---

## Framework Structure

```text
ecommerce-test-automation-suite/
│
├── config/
│   └── config.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── conftest.py
│   ├── ui/
│   │   ├── test_login.py
│   │   ├── test_cart.py
│   │   └── test_checkout.py
│   └── api/
│       └── test_api.py
│
├── utils/
│   ├── driver_factory.py
│   ├── logger.py
│   └── screenshot_helper.py
│
├── data/
│   ├── login_data.json
│   └── product_data.csv
│
├── reports/
├── screenshots/
├── logs/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── pytest.ini
├── requirements.txt
└── README.md