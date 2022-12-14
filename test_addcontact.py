import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_create_contact(page: Page):
    # test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
   
    page.get_by_text("Contacts").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/contacts")
    page.get_by_role("button", name="Add contact").click()
    page.get_by_label("First name").click()
    page.get_by_label("First name").fill("Shyam")
    page.get_by_label("Middle name").click()
    page.get_by_label("Middle name").fill("K")
    page.get_by_label("Last name*").click()
    page.get_by_label("Last name*").fill("N")
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("Shyam@gmai.in")
    page.get_by_label("Phone number*").click()
    page.get_by_label("Phone number*").fill("(234) 567-7777")
    page.locator(".date-input").click()
    page.get_by_role("option", name="Choose Tuesday, January 2nd, 1990").click()
    page.locator(".css-ackcql").click()
    page.locator("#react-select-11-option-0").click()
    page.locator("input[name=\"jurisdictionUUID\"]").click()
    page.locator("input[name=\"jurisdictionUUID\"]").fill("s")
    page.get_by_role("heading", name="Alaska").click()
    page.get_by_label("License number").click()
    page.get_by_label("License number").fill("123")
    page.get_by_label("Mailing Address").click()
    page.get_by_label("Mailing Address").fill("d")
    page.get_by_text("Dallas, TX, USA").click()
    page.get_by_label("Apt").click()
    page.get_by_label("Apt").fill("345")
    page.get_by_role("button", name="Save tick-sign").click()
    page.get_by_text("ML").first.click()
    page.get_by_role("button", name="Log out").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/")

def test_invalidcreate_contact(page: Page):
    # test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
   
    page.get_by_text("Contacts").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/contacts")
    page.get_by_role("button", name="Add contact").click()
    page.get_by_label("First name").click()
    page.get_by_label("First name").fill("Sanju")
    page.get_by_label("Middle name").click()
    page.get_by_label("Middle name").fill("M")
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("sanju@fggg")
    page.get_by_label("Phone number*").click()
    page.get_by_label("Phone number*").fill("(234) 4556")
    page.locator(".date-input").click()
    page.get_by_role("option", name="Choose Tuesday, January 2nd, 1990").click()
    page.locator(".css-ackcql").click()
    page.locator("#react-select-11-option-0").click()
    page.locator("input[name=\"jurisdictionUUID\"]").click()
    page.get_by_label("License number").click()
    page.get_by_label("License number").fill("134")
    page.get_by_role("button", name="Save tick-sign").click()
    page.get_by_label("Last name*").click()
    page.get_by_text("Last name is required").click()
    page.get_by_label("Phone number*").click()
    page.get_by_text("Phone number is not valid").click()
    page.locator("input[name=\"email\"]").click()
    page.get_by_text("Invalid email. Please try again").click()
    page.get_by_role("button", name="Save tick-sign").click()
   
