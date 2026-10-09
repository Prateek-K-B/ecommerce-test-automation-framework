"""
API test suite using DummyJSON (https://dummyjson.com), a free public
fake-data API. No API key or auth required.

Covers:
- GET request + status code + schema validation
- GET single resource + field value validation
- POST request + status code + response body validation
"""

import requests

from config import config
from utils.logger import get_logger

logger = get_logger(__name__)


def test_get_all_products_status_and_schema():
    """GET /products should return 200 and a well-formed products list."""
    response = requests.get(f"{config.API_BASE_URL}/products")
    logger.info(f"GET /products -> {response.status_code}")

    assert response.status_code == 200

    body = response.json()
    assert "products" in body
    assert isinstance(body["products"], list)
    assert len(body["products"]) > 0

    first_product = body["products"][0]
    for field in ("id", "title", "price", "category"):
        assert field in first_product, f"Missing expected field: {field}"


def test_get_single_product_by_id():
    """GET /products/{id} should return the correct product."""
    product_id = 1
    response = requests.get(f"{config.API_BASE_URL}/products/{product_id}")
    logger.info(f"GET /products/{product_id} -> {response.status_code}")

    assert response.status_code == 200

    body = response.json()
    assert body["id"] == product_id
    assert isinstance(body["title"], str) and len(body["title"]) > 0
    assert isinstance(body["price"], (int, float))


def test_get_product_not_found():
    """GET a non-existent product id should return 404."""
    response = requests.get(f"{config.API_BASE_URL}/products/999999")
    logger.info(f"GET /products/999999 -> {response.status_code}")

    assert response.status_code == 404


def test_create_product_post_request():
    """POST /products/add should accept a new product and echo it back."""
    payload = {
        "title": "Automation Test Product",
        "price": 49,
        "category": "test-automation",
    }

    response = requests.post(f"{config.API_BASE_URL}/products/add", json=payload)
    logger.info(f"POST /products/add -> {response.status_code}")

    assert response.status_code == 201

    body = response.json()
    assert body["title"] == payload["title"]
    assert body["price"] == payload["price"]
    assert "id" in body
