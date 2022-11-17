import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_dashboard(page: Page):
    test_login.test_renegade_login(page)
    
    page.wait_for_url("https://crmnext.renegadeinsurance.com/dashboard")