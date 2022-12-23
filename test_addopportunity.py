
import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_create_opportunity(page: Page):
    # test_login.test_renegade_login(page)
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
   
   
    page.get_by_text("Opportunities").first.click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/opportunities")
    page.get_by_role("button", name="Add opportunity").click()
    page.get_by_label("First name").click()
    page.get_by_label("First name").fill("dssffff")
    page.get_by_label("Last name*").click()
    page.get_by_label("Last name*").fill("cdfsdf")
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("xzcvdv@fg.in")
    page.get_by_label("Phone number*").click()
    page.get_by_label("Phone number*").fill("(345) 678-87653")
    page.locator(".css-ackcql").first.click()
    page.locator("#react-select-11-option-0").click()
    page.get_by_label("Mailing Address").click()
    page.get_by_label("Mailing Address").fill("a")
    page.get_by_text("Atlanta, GA, USA").click()
    page.locator(".css-fghkso-indicatorContainer > .css-8mmkcg").first.click()
    page.get_by_text("Opportunity source").click()
    page.get_by_text("Opportunity source").click()
    page.locator("#react-select-18-option-0-0").click()
    page.locator("input[name=\"productCategory\"]").click()
    page.locator("input[name=\"productCategory\"]").fill("a")
    page.get_by_role("heading", name="atv").click()
    page.locator(".css-14y3h8c-control > .css-15aalx3 > .css-ackcql").first.click()
    page.locator("#react-select-19-option-0").click()
    page.get_by_text("Pipeline stage *").click()
    page.locator("#react-select-20-option-0").click()
    page.locator("input[name=\"producer\"]").click()
    page.locator("input[name=\"producer\"]").fill("m")
    page.get_by_text("megha+demopa@hamon.in").click()
    page.get_by_label("Opportunity name*").click()
    page.get_by_label("Opportunity name*").fill("hai")
    page.locator("div:nth-child(2) > div > div > .d-flex > .react-datepicker-wrapper > .react-datepicker__input-container > .date-input").click()
    page.get_by_role("option", name="Choose Thursday, December 1st, 2022").click()
    page.get_by_role("button", name="Save tick-sign").click()
