from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def go_to_saucedemo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    return driver

def find_username_field(driver):

    username_field = driver.find_element(By.ID, "user-name")
    return username_field

def find_password_field(driver):

    password_field = driver.find_element(By.ID, "password")
    return password_field

def find_submit_button(driver):

    submit_button = driver.find_element(By.ID, "login-button")
    return submit_button
driver = go_to_saucedemo()

try:
    username = find_username_field(driver)
    password = find_password_field(driver)
    submit = find_submit_button(driver)

    print("Элементы найдены")

except NoSuchElementException as e:
    print(f"Элемент не найден: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")

driver.quit()