import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_create_lead(page: Page):
    test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Leads").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/mybook/leads")

    # page.get_by_role("row", name="shyam s New Personal 11/21/2022 shyam@gmail.com (345) 678-7654 Qualify vector").get_by_role("button", name="vector").click()
    # page.get_by_role("button", name="vector Edit bin Add activity plusIcon Mark as Junked junk-icon Delete bin").click()
    # page.get_by_label("First name").click()
    # page.get_by_label("First name").fill("shyamana")
    # page.get_by_role("button", name="Save tick-sign").click()

   