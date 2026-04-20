import os
import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.contact_page import ContactPage



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def contact_page(driver):
    return ContactPage(driver)

