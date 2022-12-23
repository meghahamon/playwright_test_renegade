import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_create_pipeline(page: Page):
    # test_login.test_renegade_login(page)
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="Sales Pipeline").click()
    
    page.get_by_text("Default Pipeline").click()
   
    page.get_by_text("Add new pipeline").click()
    page.get_by_text("Create a Pipeline").click()
    page.get_by_label("Pipeline Name").click()
    page.get_by_label("Pipeline Name").fill("demo")
    page.locator("#react-select-20-option-0").click()

    # page.get_by_text("Annuity").check()
    # page.locator("text=Annuity").check()
    # page.locator("input[value='Annuity']").isChecked().toBeTruthy()
    # page.locator("input[value='Annuity']").click()
    # page.get_by_role("row", name="Annuity").locator("input[type=\"checkbox\"]").check()
    # page.locator("#react-select-16-option-9").check().click()
    page.get_by_role("button", name="Save tick-sign").click()