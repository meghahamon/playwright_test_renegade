import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login



def test_edit_pipeline(page: Page):
    # test_login.test_renegade_login(page)
    page.get_by_role("img", name="logo").first.click()
    page.get_by_role("heading", name="Sales Pipeline").click()
    
    import pdb;pdb.set_trace()
    page.get_by_role("button", name="dfri").click()
    page.get_by_role("button", name="edit").first.click()