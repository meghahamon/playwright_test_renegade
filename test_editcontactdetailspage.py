import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_edit_contactdetailspage(page: Page):
    # test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Contacts").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/contacts")

    # import pdb;pdb.set_trace()
    # tr = page.locator(".table > .thead >  .tr").first
    page.locator("b:has-text(\"Sample K\")").first.click()

    page.get_by_role("img", name="edit").click()

    page.get_by_label("First name").click()
    page.get_by_label("First name").fill("hai")

    page.get_by_label("Phone number*").click()
    page.get_by_label("Phone number*").fill("(234) 090-6689")

    page.get_by_label("Last Name*").click()
    page.get_by_label("Last Name*").fill("hello")

    page.get_by_role("button", name="Save tick-sign").click()