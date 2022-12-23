import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_activity_account(page: Page):
    # test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Accounts").first.click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/accounts")

  
    action_button = page.locator(".d-flex > .vector").first
    action_button.click()

    
    page.locator("b:has-text(\"hai hello\")").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/contacts/0ef8ddce-6b63-47ec-b171-2e39c59f91c3/activities")
    # page.get_by_text("Activities0Opportunities0Accounts1Quotes0Policies0Documents0HistoryAdd NoteAdd T").first.click()
    page.get_by_role("link", name="Activities4").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/contacts/0ef8ddce-6b63-47ec-b171-2e39c59f91c3/activities")
    page.get_by_text("Add Note").first.click()
    
    page.get_by_role("paragraph").first.click()
    page.get_by_role("paragraph").first.fill('dam')
    
    

    page.get_by_role("button", name="Add Note").click()
    page.locator(".info > div > .profile-pic").first.click()
    

   