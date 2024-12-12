import pytest
from bs4 import BeautifulSoup
from unittest import mock
from project import fetch_page, parse_products, save_to_file

url = "https://www.bottleworks.com/shop/"


def test_fetch_page():
    soup = fetch_page(url)
    assert soup.find('h2', class_='woocommerce-loop-product__title') is not None

def test_parse_products():
    soup = fetch_page(url)
    search_term = "ipa"
    products = list(parse_products(soup, search_term))
    assert len(products) >= 0
    assert all(search_term in product[0].lower() for product in products)

def test_save_to_file():
    data = [("Sample IPA", "$5.00"), ("Sample Lager", "$4.00")]
    filename = "found_beers.txt"
    with mock.patch("builtins.open", mock.mock_open()) as mock_file:
        save_to_file(filename, data)
        mock_file().write.assert_any_call("Sample IPA = $5.00\n")
        mock_file().write.assert_any_call("Sample Lager = $4.00\n")

