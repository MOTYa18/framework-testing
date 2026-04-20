import pytest
from pages.locators import LocatorsHomePage
from pages.locators import LocatorsLoginPage

@pytest.mark.parametrize("email,password", 
                         [
    ("customer2@practicesoftwaretesting.com", "welcome01"),
    ("customer3@practicesoftwaretesting.com", "pass123")
]
)
def test_login_user_valid(login_page, email, password):
    login_page.open()
    login_page.login(email, password)
    login_page.wait(LocatorsLoginPage.TEXT_MY_ACCOUNT)
    assert login_page.wait(LocatorsLoginPage.TEXT_MY_ACCOUNT).is_displayed()


@pytest.mark.parametrize("email,password", 
                         [
    ("test@gmail.com", "test"),
    ("error@gmail.com", "error")
]
)

def test_login_user_no_valid(login_page, email, password):
    login_page.open()
    login_page.login(email, password)
    login_page.wait(LocatorsLoginPage.ERROR_LOCATOR)
    assert login_page.wait(LocatorsLoginPage.ERROR_LOCATOR).is_displayed()

def test_login_admin(login_page):
    login_page.open()
    login_page.login("admin@practicesoftwaretesting.com", "welcome01")
    assert login_page.wait(LocatorsLoginPage.TEXT_SALES_OVER_THE_YEARS).is_displayed()
    


    