import re
from playwright.sync_api import Page, expect, sync_playwright

from faker import Faker
import test_login



def test_qualifylead(page: Page):
    # test_login.test_renegade_login(page)

    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Leads").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/leads")

    page.locator(".td > div > .actionButton").first.click()
    page.get_by_role("button", name="Yes").click()
    fake = Faker()
    number = fake.phone_number()
    page.get_by_label("Phone number *").click()
    page.get_by_label("Phone number *").fill(number)

    page.get_by_role("button", name="Save tick-sign").click() 
    

def test_qualifylead_detailspage(page: Page):
    # test_login.test_renegade_login(page) 

    page.get_by_role("img", name="logo").first.click()   
    page.get_by_role("heading", name="My Book").click()
    page.get_by_text("Leads").click()
    page.wait_for_url("https://crm.dev.joinhobnob.com/mybook/leads")

    page.locator("b:has-text(\"Lead\")").first.click()
    page.get_by_role("button", name="Qualify lead").click()
    page.get_by_role("button", name="Yes").click()

    fake = Faker()
    number = fake.phone_number()

    page.get_by_label("Phone number *").click()     
    page.get_by_label("Phone number *").fill(number)

    page.get_by_role("button", name="Save tick-sign").click() 

    
   
