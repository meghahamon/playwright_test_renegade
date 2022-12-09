import re
from playwright.sync_api import Page, expect, sync_playwright


def test_renegade_login(page: Page):
    page.goto("https://crm.dev.joinhobnob.com/")
    page.get_by_label("Email").click()

    page.get_by_label("Email").fill("megha+demopa@hamon.in")

    page.get_by_label("Email").press("Tab")

    page.get_by_label("Password").fill("Megha12@hamon.in1")

    page.locator("input[name=\"remember\"]").check()

    page.get_by_role("button", name="Log In arrow-function").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/dashboard")

def test_renegade_invalid_login(page: Page):
    page.goto("https://crm.dev.joinhobnob.com/")
    page.get_by_label("Email").click()

    page.get_by_label("Email").fill("megha+demopa@hamon.in")

    page.get_by_label("Email").press("Tab")

    page.get_by_label("Password").fill("Megha12@ham")

    page.locator("input[name=\"remember\"]").check()

    page.get_by_role("button", name="Log In arrow-function").click()
    
    page.get_by_text("Invalid email or password. Please try again").click()

def test_admin_login(page:Page):
    page.goto("https://crm.dev.joinhobnob.com/")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("admin@joinhobnob.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("zP!!IWsU$QCSbIEY")
    page.get_by_role("button", name="Log In arrow-function").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/dashboard")