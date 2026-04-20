from pages.locators import LocatorsHomePage
from pages.locators import LocatorsLoginPage

def test_button_sign_in(home_page):
     home_page.open()
     home_page.click_sign_in()
     home_page.wait(LocatorsLoginPage.INPUT_EMAIL)
     assert home_page.get_url() == "https://practicesoftwaretesting.com/auth/login"

def test_button_categories(home_page):
     home_page.open()
     home_page.click_categories()
     assert home_page.wait(LocatorsHomePage.BUTTON_HAND_TOOLS)


def test_button_hand_tools(home_page):
     home_page.open()
     home_page.click_categories()
     home_page.click_hands_tools()
     home_page.wait(LocatorsHomePage.TEXT_HAND_TOOLS)
     assert home_page.get_url() == 'https://practicesoftwaretesting.com/category/hand-tools'