import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_commercial_opportunity(page: Page):
    # test_login.test_renegade_login(page)
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Opportunities").first.click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/opportunities")
    page.get_by_role("button", name="Add opportunity").click()
    page.get_by_text("Commercial").click()
    page.get_by_label("Last name*").click()
    page.get_by_label("Last name*").fill("sadsfr")
    page.locator(".date-input").first.click()
    page.get_by_role("option", name="Choose Monday, January 1st, 1990").click()
    page.get_by_role("textbox", name="Phone number*").click()
    page.get_by_role("textbox", name="Phone number*").fill("(234) 567-87653")
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("fghjhj@ghj.in")
   
    page.locator("input[name=\"driverLicensedState\"]").click()
    page.locator("input[name=\"driverLicensedState\"]").fill("a")
    page.get_by_role("heading", name="Alabama").click()
    page.get_by_label("License number").click()
    page.get_by_label("License number").fill("134")
    page.get_by_label("Business name*").click()
    page.get_by_label("Business name*").fill("demo")
    page.locator("input[name=\"industry\"]").click()
    page.locator("input[name=\"industry\"]").fill("c")
    page.get_by_role("heading", name="111120 - Oilseed (except Soybean) Farming").click()
    page.get_by_label("Business Phone Number*").click()
    page.get_by_label("Business Phone Number*").fill("(345) 678-76543")
    page.get_by_label("Business address").click()
    page.get_by_label("Business address").fill("we")
    page.get_by_text("Westfield, NJ, USA").click()
    page.get_by_label("Total payroll*").click()
    page.get_by_label("Total payroll*").fill("123")
    page.get_by_text("Opportunity source").click()
    page.locator("#react-select-17-option-0-0").click()
    page.locator("input[name=\"productCategory\"]").click()
    page.locator("input[name=\"productCategory\"]").fill("a")
    page.get_by_role("heading", name="auto liability").click()
    page.get_by_text("Pipeline *").click()
    page.locator("#react-select-19-option-0").click()
    page.get_by_text("Pipeline stage *").click()
    page.locator("#react-select-20-option-0").click()
    page.locator("input[name=\"producer\"]").click()
    page.locator("input[name=\"producer\"]").fill("m")
    page.get_by_text("mLmegha Lmegha+demopa@hamon.in(235) 677-8889").click()
    page.get_by_label("Opportunity name*").click()
    page.get_by_label("Opportunity name*").fill("samp")
    page.get_by_role("button", name="Save tick-sign").click()
