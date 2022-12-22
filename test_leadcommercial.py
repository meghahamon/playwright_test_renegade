import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_lead_commercial(page: Page):
    # test_login.test_renegade_login(page)

   
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Leads").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/leads")
    page.get_by_role("button", name="Add lead").click()

    page.locator("p:has-text(\"Commercial\")").click()
    page.get_by_role("img", name="drop").click()
    page.get_by_text("Facebook").click()
    page.get_by_label("First name").click()
    page.get_by_label("First name").fill("")
    page.get_by_label("Middle name").click()
    page.get_by_label("Middle name").fill("")
    page.get_by_label("Last name").click()
    page.get_by_label("Last name").fill("Lead")
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("lead@hamon.in")
    page.get_by_label("Phone number").click()
    page.get_by_label("Phone number").click()
    page.get_by_label("Phone number").fill("(234) 567-8967")
    page.locator(".css-8mmkcg").click()
    page.locator("#react-select-11-option-0").click()
    page.get_by_label("Business name").click()
    page.get_by_label("Business name").fill("demo")
    page.locator("input[name=\"industry\"]").click()
    page.locator("input[name=\"industry\"]").fill("c")
    page.get_by_role("heading", name="541511 - Custom Computer Programming Services").click()
    page.get_by_label("Business PhoneNumber").click()
    page.get_by_label("Business PhoneNumber").fill("(344) 555-6666")
    page.get_by_label("Business email").click()
    page.get_by_label("Business email").fill("demo@ghj.in")
    page.get_by_label("Business address").click()
    page.get_by_label("Business address").fill("d")
    page.get_by_text("Dallas, TX, USA").click()
    page.get_by_label("Apt").click()
    page.get_by_label("Apt").fill("123")
    page.get_by_role("button", name="Save tick-sign").click()

def test_invalid_lead_commercial(page: Page):
    test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Leads").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/leads")
    page.get_by_role("button", name="Add lead").click()

    
    
    page.locator("p:has-text(\"Commercial\")").click()
    page.get_by_role("img", name="drop").click()
    page.get_by_text("Facebook").click()
    page.get_by_label("First name").click()
    page.get_by_label("First name").fill("sanjay")
    page.get_by_label("Middle name").click()
    page.get_by_label("Middle name").fill("k")
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("sanjay@gmail.com")
    page.get_by_label("Phone number").click()
    page.get_by_label("Phone number").fill("(234) 456-66")
    page.get_by_role("button", name="Save tick-sign").click()
    page.get_by_label("Phone number").click()
    page.get_by_text("Phone number is not valid").click()
    page.locator(".css-15aalx3").click()
    page.locator("form div:has-text(\"option New focused, 1 of 5. 5 results available. Use Up and Down to choose optio\")").nth(1).click()
    page.get_by_text("Please select a Stage").click()
    page.get_by_text("Please enter Business Name").click()
    page.get_by_text("Please enter Business Name").click()
    page.get_by_label("Business PhoneNumber").click()
    page.get_by_text("Please enter Business Phone Number").click()
    page.get_by_role("button", name="Save tick-sign").click()
   
