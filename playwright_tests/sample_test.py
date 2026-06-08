
from playwright.sync_api import Page

def test_google(page: Page):
    page.goto("https://google.com")
    assert "Google" in page.title()
