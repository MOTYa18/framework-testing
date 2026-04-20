from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LocatorsHomePage
from pages.base_page import BasePage
from pages.locators import URL
from pages.locators import LocatorsContactPage

class ContactPage(BasePage):
    def open(self):
        self.driver.get(URL.СONTACT_URL)

    def click_first_name(self):
        self.wait(LocatorsContactPage.INPUT_FIRST_NAME).click()
        
    def click_last_name(self):
        self.wait(LocatorsContactPage.INPUT_LAST_NAME).click()
    
    def click_email(self):
        self.wait(LocatorsContactPage.INPUT_EMAIL).click()
    
    def click_subject(self):
        self.wait(LocatorsContactPage.SELECT_SUBJECT).click()

    def click_customer(self):
        self.wait(LocatorsContactPage.CUSTOMER_SERVICE).click()
    
    def click_message(self):
        self.wait(LocatorsContactPage.INPUT_MESSAGE).click()

    def click_send(self):
        self.wait(LocatorsContactPage.BUTTON_SEND).click()

    def write_form(self, first_name, last_name, email, message):
        self.write(LocatorsContactPage.INPUT_FIRST_NAME, first_name)
        self.write(LocatorsContactPage.INPUT_LAST_NAME, last_name)
        self.write(LocatorsContactPage.INPUT_EMAIL, email)
        self.click_subject()
        self.click_customer()
        self.write(LocatorsContactPage.INPUT_MESSAGE, message)

    

    

    


