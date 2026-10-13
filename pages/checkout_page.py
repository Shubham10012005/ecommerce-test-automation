
from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        self.checkout_button = page.locator(
            '[data-test="checkout"]'
        )
        self.first_name = page.locator(
            '[data-test="firstName"]'
        )
        self.last_name = page.locator(
            '[data-test="lastName"]'
        )
        self.postal_code = page.locator(
            '[data-test="postalCode"]'
        )
        self.continue_button = page.locator(
            '[data-test="continue"]'
        )
        self.error_message = page.locator(
            '[data-test="error"]'
        )
        self.finish_button = page.locator(
            '[data-test="finish"]'
        )
        self.complete_header = page.locator(
            '[data-test="complete-header"]'
        )

    def start_checkout(self):
        self.checkout_button.click()

    def enter_customer_details(
        self, first_name: str, last_name: str, postal_code: str
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()
