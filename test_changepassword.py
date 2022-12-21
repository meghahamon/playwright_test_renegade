import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login

def test_change_password(page: Page):
    # test_login.test_renegade_login(page)

    page.goto("https://crm.dev.joinhobnob.com/")

   
    page.get_by_text("MQ").first.click()
    page.get_by_role("button", name="Change Password").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/myprofile/changepassword")
   

    page.get_by_text("Change passwordForgot current password? You can Reset Password via EmailCurrent").click()
    page.locator("input[name=\"currentPassword\"]").click()
    page.locator("input[name=\"currentPassword\"]").fill("Megha12@hamon.in1")
    page.locator("input[name=\"newPassword\"]").click()
    page.locator("input[name=\"newPassword\"]").fill("Megha12@hamon.in1")
    page.locator("input[name=\"confirmPassword\"]").click()
    page.locator("input[name=\"confirmPassword\"]").fill("Megha12@hamon.in")

    page.get_by_role("button", name="Change password arrow-function").click()
    page.get_by_text("ML").first.click()
    page.get_by_role("button", name="Log out").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/")