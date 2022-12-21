import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_create_account(page: Page):
    # test_login.test_renegade_login(page)
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
   
   
    page.get_by_text("Accounts").first.click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/accounts")
    page.locator("div:nth-child(3) > img").first.click()
    page.locator(".css-ackcql").first.click()
    page.locator("#react-select-11-option-0").click()
    page.locator(".css-15aalx3 > .css-ackcql").first.click()
    page.locator("#react-select-11-option-0").click()
    page.locator(".css-1r3mo5p-placeholder").first.click()
    page.locator("#react-select-11-option-0").click()
    page.locator("input[name=\"producer\"]").first.click()
    page.locator("input[name=\"producer\"]").first.fill("m")
    page.get_by_text("megha+demopa@hamon.in(345) 678-7654").click()
    page.get_by_text("4 filters added").first.click()
    page.get_by_role("button", name="Clear all filters").click()
    page.get_by_text("ML").first.click()
    page.get_by_role("button", name="Log out").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/")