
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_with_valid_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
    expect(page.locator('[data-test="title"]')).to_have_text("Products")


@pytest.mark.regression
def test_login_with_invalid_password(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_password")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).not_to_be_empty()
