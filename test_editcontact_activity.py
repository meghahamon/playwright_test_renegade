import re
from playwright.sync_api import Page, expect, sync_playwright
# from faker import Faker
import test_login



def test_activity_contact(page: Page):
    test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Contacts").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/contacts")
    # fake = Faker()
    # text=fake.text()
    # import pdb;pdb.set_trace()
    page.locator("b:has-text(\"sanju samson\")").first.click()

    
    page.get_by_text("Activities 1").click()
    page.get_by_text("Add Note").first.click()
   
    
    page.get_by_role("heading", name="All Activities").click()
    
    page.get_by_role("heading", name="Rohith Samuel").first.click()
    # import pdb;pdb.set_trace()

    page.locator(".d-flex > button:nth-child(4)").first.click()
    print(1)
    
    page.locator("text=Edit").click()
    print(3)