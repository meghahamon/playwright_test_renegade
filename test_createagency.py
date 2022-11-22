import re
from playwright.sync_api import Page, expect, sync_playwright
from faker import Faker
import test_login

def test_createagency(page: Page):
    test_login.test_admin_login(page)


    # import pdb; pdb.set_trace()
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("link", name="logo Management").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/admin")
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="Manage Agencies").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/admin/agency")
    page.get_by_role("button", name="Add Agency add").click()

    fake = Faker()
    name=fake.name()
    email=fake.email()

    page.get_by_label("Agency Name").click()
    page.get_by_label("Agency Name").fill("asherty")

    page.locator("form").get_by_text("User Group").click()

    page.locator("#react-select-11-option-0").click()
    page.get_by_text("Sub Group").click()

    page.locator("#react-select-12-option-0").click()
    page.get_by_label("First Name").click()
    page.get_by_label("First Name").fill(name)

    page.get_by_label("Middle Name").click()
    page.get_by_label("Middle Name").fill("S")

    page.get_by_label("Last Name").click()
    page.get_by_label("Last Name").fill("E")

    page.get_by_label("Email").click()
    page.get_by_label("Email").fill(email)

    page.get_by_label("Phone Number").click()
    page.get_by_label("Phone Number").fill("(234) 567-88764")

    page.get_by_role("button", name="Save tick-sign").click()
    page.get_by_text("Success").click()
    # page.get_by_text("Agency asherty has been created and invitation link has been sent to f'{email}'").click()

    