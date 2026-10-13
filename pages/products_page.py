
from playwright.sync_api import Page, expect


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    def sort_products_low_to_high(self):
        self.sort_dropdown.select_option("lohi")

    def add_product_to_cart(self, product_name: str):
        product = self.page.locator(".inventory_item").filter(
            has_text=product_name
        )
        product.locator("button").click()

    def remove_product_from_cart(self, product_name: str):
        product = self.page.locator(".inventory_item").filter(
            has_text=product_name
        )
        product.locator("button").click()

    def open_cart(self):
        self.cart_link.click()
