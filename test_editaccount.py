import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_edit_account(page: Page):
    # test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Accounts").first.click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/accounts")
   
    action_button = page.locator(".d-flex > .vector").first

    action_button.click()
   
    edit_button = action_button.get_by_text("Edit").first.click()
 
    page.get_by_label("First name").click()
    
    page.get_by_label("First name").fill("k")
    
    # page.get_by_role("button", name="Save tick-sign").click()