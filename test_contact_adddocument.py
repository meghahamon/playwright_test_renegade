
import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_contact_adddocument(page: Page):
    # test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Contacts").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/contacts")

    # import pdb;pdb.set_trace()
   
    
    page.locator("b:has-text(\"Jennifer Bryant Lead\")").click()
    print(1)
    page.wait_for_url("https://crm.dev.joinhobnob.com/contacts/91033dd3-dfb6-40f1-b57c-62059f4d9774/activities")
    print(2)
    page.get_by_role("link", name="Documents1").click()
    print(3)
    page.wait_for_url("https://crm.dev.joinhobnob.com/contacts/91033dd3-dfb6-40f1-b57c-62059f4d9774/documents")
    print(4)
    page.get_by_role("button", name="Add documents").click()
    print(5)
    page.get_by_role("button", name="Browse files").click()
    print(6)
    page.locator("input[type=\"file\"]").set_input_files("/home/megha/Documents/HT_3_Grp_hallticket.pdf")
    print(7)
    page.get_by_role("button", name="Document type").click()
    print(8)
    page.get_by_role("button", name="Signed application").first.click()
    print(9)
    page.get_by_role("button", name="Save tick-sign").click()
    print(10)
   

  
   