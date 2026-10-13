
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage


def test_checkout_requires_first_name(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.add_product_to_cart("Sauce Labs Backpack")
    products.open_cart()

    checkout = CheckoutPage(page)
    checkout.start_checkout()
    checkout.enter_customer_details("", "Tester", "400001")
    checkout.continue_checkout()

    expect(checkout.error_message).to_be_visible()
    expect(checkout.error_message).to_contain_text(
        "First Name is required"
    )


def test_complete_checkout(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.add_product_to_cart("Sauce Labs Backpack")
    products.open_cart()

    checkout = CheckoutPage(page)
    checkout.start_checkout()
    checkout.enter_customer_details(
        "QA", "Tester", "400001"
    )
    checkout.continue_checkout()
    checkout.finish_order()

    expect(checkout.complete_header).to_have_text(
        "Thank you for your order!"
    )
