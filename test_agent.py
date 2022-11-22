import re
from playwright.sync_api import Page, expect, sync_playwright
from faker import Faker
import test_login

def test_create_agent(page: Page):
    test_login.test_admin_login(page)
    
    page.goto("https://crmnext.renegadeinsurance.com/")

    
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("link", name="logo Management").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/admin")
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="Manage Agencies").click()
    
    page.wait_for_url("https://crmnext.renegadeinsurance.com/admin/agency")

    page.locator(".td > .d-flex > .actionButton").first.click()
    # page.wait_for_url("https://crmnext.renegadeinsurance.com/admin/agency/52848194-93ab-4d52-9a78-4a12b807631b/user")
    page.get_by_role("button", name="Add User add").click()
    fake = Faker()
    name=fake.name()
    email=fake.email()
    page.get_by_label("First Name").click()
    page.get_by_label("First Name").fill(name)
    page.get_by_label("Middle Name").click()
    page.get_by_label("Middle Name").fill("ali")
    page.get_by_label("Last Name").click()
    page.get_by_label("Last Name").fill("ha")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill(email)
    page.get_by_label("Phone Number").click()
    page.get_by_label("Phone Number").fill("(365) 677-85677")
    page.get_by_text("Location").click()
    page.locator("#react-select-11-option-0").click()
    page.get_by_text("Select a role").click()
    page.locator("#react-select-12-option-0").click()
    page.get_by_role("button", name="Save tick-sign").click()
    page.get_by_text("Success").click()
  

    page.get_by_text(f'{name} ha has been added as a user for Renegade Team.').click()

    page.get_by_role("cell", name=f'{name} ha').click()
   
   
   
    
    

   


