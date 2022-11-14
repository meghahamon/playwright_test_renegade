import re
from playwright.sync_api import Page, expect, sync_playwright



def test_renegade_reset_password(page: Page):
    page.goto("https://crmnext.renegadeinsurance.com/")

    page.get_by_role("button", name="Reset Password").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/reset-password")
    page.get_by_label("Email").click()

    page.get_by_label("Email").fill("rohith@hamon.in")

    page.get_by_role("button", name="Reset Password arrow-function").click()

    page.get_by_text("An email with the instructions to reset the password has been sent to rohith@hamon.in").click()
    page.get_by_text("Can't find the mail? Check your spam folder. It was sent from support@renegadein").click()
    page.get_by_role("button", name="Back to Log In").click()
    page.wait_for_url("https://crmnext.renegadeinsurance.com/")
