import re
from playwright.sync_api import Page, expect, sync_playwright
from faker import Faker
import test_login



def test_create_principalagent(page: Page):
    test_login.test_admin_login(page)
    
    page.goto("https://crmnext.renegadeinsurance.com/")

    # import pdb; pdb.set_trace()
   
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("link", name="logo Management").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/admin")
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="Manage Agencies").click()
    
    page.wait_for_url("https://crmnext.renegadeinsurance.com/admin/agency")
    
    page.locator(".td > .d-flex > .actionButton").first.click()
    # page.wait_for_url("https://crmnext.renegadeinsurance.com/admin/agency/eaaccf71-3bf6-4140-9fec-e7ba9678f1ee/user")
    page.get_by_role("button", name="Add User add").click()
    fake = Faker()
    name=fake.name()
    email=fake.email()
    page.get_by_label("First Name").click()
    page.get_by_label("First Name").fill(name)
    page.get_by_label("Middle Name").click()
    page.get_by_label("Middle Name").fill("K")
    page.get_by_label("Last Name").click()
    page.get_by_label("Last Name").fill("P")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill(email)
    page.get_by_label("Phone Number").click()
    page.get_by_label("Phone Number").fill("(456) 888-55888")
    page.get_by_text("Location").click()
    page.locator("#react-select-11-option-0").click()
    page.get_by_text("Select a role").click()
    page.locator("#react-select-12-option-1").click()
    page.get_by_role("button", name="Save tick-sign").click()
    page.get_by_text("Success").click()
    page.get_by_text(f'{name} P has been added as a user for Renegade Team.').click()
    # import pdb; pdb.set_trace()
    # page.get_by_text(f'{name} P').click()
    page.get_by_role("cell", name=f'{name} P').click()
    # row_config = f'tr:has-text("{name} P")'
    # row = page.locator(row_config)
    # row.innertext()
    


