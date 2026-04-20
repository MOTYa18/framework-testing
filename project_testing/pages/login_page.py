from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LocatorsHomePage
from pages.locators import LocatorsLoginPage
from pages.base_page import BasePage
from pages.locators import URL

class LoginPage(BasePage):
    def open(self):
        self.driver.get(URL.LOGIN_URL)

    def click_input_email(self):
        self.wait(LocatorsLoginPage.INPUT_EMAIL).click()
        
    def click_input_password(self):
        self.wait(LocatorsLoginPage.INPUT_PASSWORD).click()

    def click_button_login(self):
        self.wait(LocatorsLoginPage.BUTTON_LOGIN).click()
    
    def login(self, email, password):
        self.write(LocatorsLoginPage.INPUT_EMAIL, email)
        self.write(LocatorsLoginPage.INPUT_PASSWORD, password)
        self.click_button_login()




    

    

    
        