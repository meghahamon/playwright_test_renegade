import re
from playwright.sync_api import Page, expect, sync_playwright


def test_renegade_login(page: Page):
    page.goto("https://crmnext.renegadeinsurance.com/")
    page.get_by_label("Email").click()

    page.get_by_label("Email").fill("rohith@hamon.in")

    page.get_by_label("Email").press("Tab")

    page.get_by_label("Password").fill("123456789!Qa")

    page.locator("input[name=\"remember\"]").check()

    page.get_by_role("button", name="Log In arrow-function").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/dashboard")

def test_renegade_invalid_login(page: Page):
    page.goto("https://crmnext.renegadeinsurance.com/")
    page.get_by_label("Email").click()

    page.get_by_label("Email").fill("rohith@hamon.in")

    page.get_by_label("Email").press("Tab")

    page.get_by_label("Password").fill("123456789")

    page.locator("input[name=\"remember\"]").check()

    page.get_by_role("button", name="Log In arrow-function").click()
    
    page.get_by_text("Invalid email or password. Please try again").click()

def test_admin_login(page:Page):
    page.goto("https://crmnext.renegadeinsurance.com/")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("demo@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("demopass")
    page.get_by_role("button", name="Log In arrow-function").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/dashboard")