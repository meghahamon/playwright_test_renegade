import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_viewcontact_detailspage(page: Page):
    # test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Contacts").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/contacts")

    # import pdb;pdb.set_trace()
   
    page.locator("b:has-text(\"Lead\")").first.click()

    
    # page.locator("b:has-text(\"Jennifer Bryant Lead\")").click()
    # page.wait_for_url("https://crm.dev.joinhobnob.com/contacts/91033dd3-dfb6-40f1-b57c-62059f4d9774/activities")
    # page.get_by_role("link", name="Activities1").click()
    # page.wait_for_url("https://crm.dev.joinhobnob.com/contacts/91033dd3-dfb6-40f1-b57c-62059f4d9774/activities")

    page.get_by_text("Activities 1").click()
    page.get_by_text("Add Note").first.click()
   
    
    page.get_by_role("heading", name="All Activities").click()
    
    page.get_by_role("heading", name="megha qw").first.click()
    
    