import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_contact_adddocument(page: Page):
    # test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Contacts").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/contacts")
    
    page.locator("div:nth-child(3) > img").first.click()
    page.locator("input[type=\"text\"]").first.click()
    page.locator("input[type=\"text\"]").first.fill("a")
    page.get_by_role("heading", name="Alabama").click()
    page.locator("input[name=\"producer\"]").first.click()
    page.locator("input[name=\"producer\"]").first.fill("m")
    page.get_by_text("megha+demopa@hamon.in(345) 678-7654").click()
    page.get_by_text("2 filters added").first.click()
    