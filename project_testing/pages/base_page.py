from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait(self, element):
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)
        return wait.until(EC.visibility_of_element_located(element))
    
    def get_url(self):
        return self.driver.current_url
    
    def write(self, locator, text):
        self.wait(locator).send_keys(text)