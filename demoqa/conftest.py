import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def driver():
    service = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()