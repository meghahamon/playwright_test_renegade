import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login

def test_create_agency(page: Page):
    test_login.test_admin_login(page)
    
    page.goto("https://crmnext.renegadeinsurance.com/")

    page.wait_for_url("https://crmnext.renegadeinsurance.com/dashboard")

    page.get_by_role("link", name="logo Management").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/admin")

    page.get_by_role("heading", name="Manage Agencies").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/admin/agency")

    page.get_by_role("row", name="Sample Invited 11/15/2022 Group1 G1-SG1 KV +2 View users").get_by_text("View users").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/admin/agency/ae4b4a2c-1313-48a6-a403-99d6fea7ef57/user")

    page.get_by_role("button", name="Add User add").click()

    page.get_by_label("First Name").click()

    page.get_by_label("First Name").fill("Geetha")

    page.get_by_label("Middle Name").click()

    page.get_by_label("Middle Name").fill("K")

    page.get_by_label("Last Name").click()

    page.get_by_label("Last Name").fill("L")

    page.get_by_label("Email").click()

    page.get_by_label("Email").fill("ggetha@hmail.com")

    page.get_by_label("Phone Number").click()

    page.get_by_label("Phone Number").fill("(234) 567-89874")

    page.get_by_text("Location").click()

    page.locator("#react-select-11-option-0").click()

    page.get_by_text("Select a role").click()

    page.locator("#react-select-12-option-0").click()

    page.get_by_role("button", name="Save tick-sign").click()

    page.get_by_text("Success").click()

    page.get_by_text("Geetha L has been added as a user for Renegade Team.").click()

   