import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_delete_contact(page: Page):
    test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Contacts").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/contacts")

    # import pdb;pdb.set_trace()
    action_button = page.locator(".d-flex > .vector").first
   
    action_button.click()
    

    action_button.locator(':has-text("Delete")').last.click()
    
    page.get_by_role("button" , name="Delete").click()
    
    # page.get_by_text("Success").click()
    