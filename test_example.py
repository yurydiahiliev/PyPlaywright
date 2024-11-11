import re

from playwright.sync_api import expect, Page

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    page.wait_for_load_state("networkidle")
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("link", name="Get started").click()
    page.wait_for_selector("text=Installation")
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
