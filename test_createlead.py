import re
from playwright.sync_api import Page, expect, sync_playwright

from faker import Faker
import test_login




def test_create_lead(page: Page):
    test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Leads").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/leads")
    page.get_by_role("button", name="Add lead").click()

    page.get_by_text("Lead Source:").click()
    page.get_by_text("Facebook").click()
    fake = Faker()
    name =fake.name()
    email= fake.email()
    number = fake.phone_number() 
    
    page.get_by_label("First name").click()
    page.get_by_label("First name").fill(name)
    page.get_by_label("Middle name").click()
    page.get_by_label("Middle name").fill("")
    page.get_by_label("Last name").click()
    page.get_by_label("Last name").fill("Lead")
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill(email)
    page.get_by_label("Phone number").click()
    page.get_by_label("Phone number").fill(number)
    page.locator(".css-8mmkcg").click()
    page.locator("#react-select-11-option-0").click()
    page.get_by_label("Mailing Address").click()
    page.get_by_label("Mailing Address").fill("san")
    page.get_by_text("San Francisco, CA, USA").click()
    page.get_by_label("Apt").click()
    page.get_by_label("Apt").fill("456")
   
    page.get_by_role("button", name="Save tick-sign").click()

    page.get_by_text("Success adding lead!").click()

   

def test_create_invalidlead(page: Page):
    test_login.test_renegade_login(page)
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    
    page.get_by_text("Leads").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/leads")
    page.get_by_role("button", name="Add lead").click()
    page.get_by_text("Lead Source:").click()
    page.get_by_text("Facebook").click()
    page.get_by_label("First name").click()
    page.get_by_label("First name").fill("saritha")
    page.get_by_label("Middle name").click()
    page.get_by_label("Middle name").fill("ww")
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("asddf")
    page.get_by_label("Phone number").click()
    page.get_by_label("Phone number").fill("(245) 555 67")
    page.get_by_label("Mailing Address").click()
    page.get_by_label("Mailing Address").fill("san")
    page.get_by_text("San Francisco, CA, USA").click()
    page.get_by_label("Apt").click()
    page.get_by_label("Apt").fill("234")
    page.get_by_role("button", name="Save tick-sign").click()
    page.get_by_label("Last name").click()
    page.get_by_text("Last name is required").click()
    page.get_by_label("Phone number").click()
    page.get_by_label("Phone number").fill("(233) 444-4")
    page.get_by_role("button", name="Save tick-sign").click()
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("asddf@gmail.in")
    page.get_by_role("button", name="Save tick-sign").click()
    page.get_by_label("Phone number").click()
    page.get_by_text("Phone number is not valid").click()
    page.get_by_text("Lead status").click()
    page.locator("form div:has-text(\"option New focused, 1 of 5. 5 results available. Use Up and Down to choose optio\")").nth(1).click()
    page.get_by_text("Please select a Stage").click()

  