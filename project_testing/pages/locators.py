from selenium.webdriver.common.by import By

class URL:
    BASE_URL = 'https://practicesoftwaretesting.com'
    LOGIN_URL = 'https://practicesoftwaretesting.com/auth/login'
    СONTACT_URL = 'https://practicesoftwaretesting.com/contact'

class LocatorsHomePage:
    BUTTON_SIGN_IN = (By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/a')
    BUTTON_CATEGORIES = (By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/button')
    BUTTON_HAND_TOOLS = (By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/ul/li[1]/a')
    TEXT_HAND_TOOLS = (By.XPATH, '/html/body/app-root/div[2]/app-category/div[1]/h2')

class LocatorsLoginPage:
    INPUT_EMAIL = (By.XPATH, '//*[@id="email"]')
    INPUT_PASSWORD = (By.XPATH, '//*[@id="password"]')
    BUTTON_LOGIN = (By.XPATH, '/html/body/app-root/div[2]/app-login/div/div/div/form/div[3]/input')
    TEXT_SALES_OVER_THE_YEARS = (By.XPATH, '/html/body/app-root/div[2]/app-dashboard/h1')
    TEXT_MY_ACCOUNT = (By.XPATH, '/html/body/app-root/div[2]/app-overview/h1')
    ERROR_LOCATOR = (By.XPATH, '/html/body/app-root/div[2]/app-login/div/div/div/div[4]/div')

class LocatorsContactPage:
    INPUT_FIRST_NAME = (By.XPATH, '//*[@id="first_name"]')
    INPUT_LAST_NAME = (By.XPATH, '//*[@id="last_name"]')
    INPUT_EMAIL = (By.XPATH, '//*[@id="email"]')
    INPUT_MESSAGE = (By.XPATH, '//*[@id="message"]')
    SELECT_SUBJECT = (By.XPATH, '//*[@id="subject"]')
    CUSTOMER_SERVICE = (By.XPATH, '//*[@id="subject"]/option[2]')
    BUTTON_SEND = (By.XPATH, '/html/body/app-root/div[2]/app-contact/div/div/div/form/div/div[2]/div[4]/input')
    CHECK_SEND_CONTACT = (By.XPATH, '/html/body/app-root/div[2]/app-contact/div/div/div/div')
