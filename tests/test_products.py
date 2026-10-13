import pytest

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.regression
def test_sort_products_low_to_high(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.sort_products_low_to_high()

    prices = page.locator(".inventory_item_price").all_text_contents()
    numeric_prices = [float(price.replace("$", "")) for price in prices]

    assert numeric_prices == sorted(numeric_prices)


@pytest.mark.regression
def test_add_and_remove_product_from_cart(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.add_product_to_cart("Sauce Labs Backpack")

    expect(products.cart_badge).to_have_text("1")

    products.remove_product_from_cart("Sauce Labs Backpack")

    expect(products.cart_badge).to_have_count(0)
