import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_viewlead_detailspage(page: Page):
    test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Leads").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/leads")

    # import pdb;pdb.set_trace()
   
    page.locator("b:has-text(\"Lead\")").first.click()

    
    page.get_by_text("Activities 1").click()
    page.get_by_text("Add Note").first.click()
   
    
    page.get_by_role("heading", name="All Activities").click()
    
    page.get_by_role("heading", name="megha qw").first.click()
    
    