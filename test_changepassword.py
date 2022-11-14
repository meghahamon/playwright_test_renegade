import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login

def test_renegade_reset_password(page: Page):
    test_login.test_renegade_login(page)

    page.goto("https://crmnext.renegadeinsurance.com/")

    page.get_by_role("img", name="profilepic").click()
    
    page.get_by_role("button", name="Change Password").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/myprofile/changepassword")
    page.get_by_role("img", name="profilepic").click()

    page.get_by_text("Change passwordForgot current password? You can Reset Password via EmailCurrent").click()
    page.locator("input[name=\"currentPassword\"]").click()
    page.locator("input[name=\"currentPassword\"]").fill("Rohith@123")
    page.locator("input[name=\"newPassword\"]").click()
    page.locator("input[name=\"newPassword\"]").fill("123456789!Qa")
    page.locator("input[name=\"confirmPassword\"]").click()
    page.locator("input[name=\"confirmPassword\"]").fill("123456789!Qa")

    page.get_by_role("button", name="Change password arrow-function").click()