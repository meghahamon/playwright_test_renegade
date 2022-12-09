
import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_lead_adddocument(page: Page):
    test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Leads").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/leads")

    # import pdb;pdb.set_trace()
   
    page.locator("b:has-text(\"Lead\")").first.click()
    

    page.get_by_text("Documents 1").click()
   
    page.get_by_role("button", name="Add documents").click()
 
    page.get_by_role("button", name="Browse files").click()
   
    page.locator("input[type=\"file\"]").set_input_files("/home/megha/Documents/HT_3_Grp_hallticket.pdf")
  
    page.get_by_role("button", name="Document type").first.click()
   
    

    page.locator(':has-text("Signed application")').first.click()
 
   
   
    
    
    page.get_by_role("button", name="Save tick-sign").click()
  
   