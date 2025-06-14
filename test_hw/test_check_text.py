from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseComponent:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.wait = WebDriverWait(driver, 10)

    def find_element(self):
        return self.wait.until(EC.presence_of_element_located(self.locator))

    def get_text(self):
        return str(self.find_element().text)

    def click(self):
        element = self.wait.until(EC.element_to_be_clickable(self.locator))
        element.click()