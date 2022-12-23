
import re
from playwright.sync_api import Page, expect, sync_playwright
import test_login,test_dashboard,test_createlead



def test_initial(page: Page):
    test_login.test_renegade_login(page)
    test_login.test_renegade_invalid_login(page)
   
    test_dashboard.test_dashboard(page)
    test_createlead.test_create_lead(page)
    test_create_lead.test_create_invalidlead(page)
    test_leadcommercial.test_test_lead_commercial(page)
    test_lead_commercial.test_invalid_lead_commercial(page)
    test_editlead.test_edit_lead(page)
    test_leadactivity.test_activity_lead(page)
    test_junklead.test_junk_lead(page)
    test_qualifylead.test_qualifylead(page)
    test_qualifylead.test_qualifylead_detailspage(page)
    test_viewlead_detailspage.test_viewlead_detailspage(page)
    test_lead_adddocument.test_lead_adddocument(page)
    test_lead_filter.test_lead_filter(page)

    test_addcontact.test_addcontact(page)
    test_addcontact.test_invalidcreate_contact(page)
    test_contactcommercial.test_contactcommercial(page)
    test_contactcommercial.test_invalidcommercial_contact
    test_contactcommercial.test_invalidbusiness_Contact(page)
    test_editcontact.test_editcontact(page)
    test_editcontact_activity.test_editcontact_activity(page)
    test.deletecontact.test_deletecontact(page)
    test_editcontactdetailspage.test_editcontactdetailspage(page)
    test_contact_viewdetailspage.test_contact_viewdetailspage(page)
    test_contact_adddocument.test_contact_adddocument(page)
    test_contact_filter.test_contact_filter(page)

    test_addaccount.test_create_account(page)
    test_addaccount.test_create_invalidaccount(page)
    test_accountcommercial.test_accountcommercial(page)
    test_accountcommercial.test_invalidcommercial_account(page)
    test_accountcommercial.test_invalidbusiness_account(page)
    test_deleteaccount.test_deleteaccount(page)
    test_account_filter.test_account_filter(page)

    test_addpolicy.test_addpolicy(page)

    test_addopprtunity.test_addopprtunity(page)
    test_opportunitycommercial.test_commercial_opportunity(page)
    
    test_addpipeline.test_create_pipeline(page)
    test_editpipeline.test_edit_pipeline

    test_login.test_renegade_logout(page)

    test_login.test_admin_login(page)

    test_createagency.test_createagency(page)
    test_createagent.test_createagent(page)
    test_createprincipalagent.test_createprincipalagent(page)

    test_login.test_admin_logout(page)    