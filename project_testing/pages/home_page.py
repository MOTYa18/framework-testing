from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LocatorsHomePage
from pages.base_page import BasePage
from pages.locators import URL

class HomePage(BasePage):
    def open(self):
        return self.driver.get(URL.BASE_URL)
    
    def click_sign_in(self):
        self.wait(LocatorsHomePage.BUTTON_SIGN_IN).click()
        
    def click_categories(self):
        self.wait(LocatorsHomePage.BUTTON_CATEGORIES).click()

    def click_hands_tools(self):
        self.wait(LocatorsHomePage.BUTTON_HAND_TOOLS).click()
