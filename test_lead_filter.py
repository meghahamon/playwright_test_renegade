import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_lead_adddocument(page: Page):
    # test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Leads").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/leads")
    
    page.locator("div:nth-child(3) > img").first.click()
    page.locator(".css-ackcql").first.click()
    page.locator("#react-select-11-option-0").click()
    page.locator(".css-1r3mo5p-placeholder").first.click()
    page.locator("#react-select-11-option-1").click()
    page.locator(".css-1r3mo5p-placeholder").first.click()
    page.locator("#react-select-11-option-0").click()
    page.locator("input[name=\"producer\"]").first.click()
    page.locator("input[name=\"producer\"]").first.fill("m")
    page.get_by_text("mqmegha qwmegha+demopa@hamon.in(345) 678-7654").click()
    page.get_by_text("4 filters added").first.click()
