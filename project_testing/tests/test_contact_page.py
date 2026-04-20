import pytest
from pages.locators import LocatorsHomePage
from pages.locators import LocatorsLoginPage
from pages.locators import LocatorsContactPage

def test_form(contact_page):
    contact_page.open()
    contact_page.write_form("Matvey", "Zinovyev", "test@gmail.com", "Hello, RedSoft, dssdcsdcsdcsdcdscdscdcsdcdscdscsdcsdcsdcdscdscsdcsdcsdcdscsd" \
    "sdcsdcsdcsdcsdcdscsdsdcsdcsdcsdcdscdcscsdcsdcsdcsdcsdcsdcdscdscdcdscscsdcsdcsdcsdcsdcsdcdsc")
    contact_page.click_send()
    assert contact_page.wait(LocatorsContactPage.CHECK_SEND_CONTACT).is_displayed()