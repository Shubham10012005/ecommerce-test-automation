
import pytest


@pytest.fixture
def context(browser):
    context = browser.new_context(
        record_video_dir="reports/videos"
    )
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()
