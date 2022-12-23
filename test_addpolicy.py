import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login

def test_create_policy(page: Page):
    # test_login.test_renegade_login(page)
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
   
   
  

   
    page.locator(".drop-Div > div:nth-child(3)").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/policies")
    page.get_by_role("button", name="Add policy").click()
    page.locator("input[name=\"contact\"]").click()
    page.get_by_role("heading", name="Add new contact").click()
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("sfsdfg@dfgfh.in")
    page.get_by_label("Last name*").click()
    page.get_by_label("Last name*").fill("sssdsd")
    page.get_by_label("Phone number*").click()
    page.get_by_label("Phone number*").fill("(234) 578-98767")
    page.locator(".select__value-container").click()
    page.locator("#react-select-16-option-1").click()
    page.get_by_role("button", name="Next").click()
    page.locator("input[name=\"agentUUID\"]").click()
    page.locator("input[name=\"agentUUID\"]").fill("me")
    page.get_by_text("megha+demopa@hamon.in(235) 677-8889").click()
    page.locator("input[name=\"carrierUUID\"]").click()
    page.locator("input[name=\"carrierUUID\"]").fill("s")
    page.get_by_label("Policy Number*").click()
    page.get_by_label("Policy Number*").fill("234")
    page.get_by_text("Policy Term *").click()
    page.locator("#react-select-19-option-0").click()
    page.locator("input[name=\"effectiveDate\"]").click()
    page.get_by_role("option", name="Choose Wednesday, December 21st, 2022").click()
    # page.locator("div:nth-child(8)").click()
    page.locator("input[name=\"expiryDate\"]").click()
  
    page.locator(".scroll-bar > div > div:nth-child(5)").click()
    page.locator("#billType svg").click()
    page.locator("#react-select-20-option-0").click()
    page.get_by_text("BASIC INFOHO3Select producer*Policy sold throughPolicy sold throughDirectly appo").click()
    page.get_by_label("Premium amount*").click()
    page.get_by_label("Premium amount*").fill("234")
    page.get_by_role("button", name="Add HO3").click()
    page.get_by_role("button", name="cross-icon").nth(1).click()
   
   