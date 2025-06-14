import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent


class TestCheckText:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_footer_text(self):
        self.driver.get('https://demoqa.com/')

        footer = BaseComponent(self.driver, (By.CSS_SELECTOR, "footer span"))

        expected_text = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."
        actual_text = footer.get_text()

        assert actual_text == expected_text, f"Ожидался текст: '{expected_text}', получен: '{actual_text}'"

    def test_elements_page_center_text(self):
        # Переход на главную страницу
        self.driver.get('https://demoqa.com/')

        # Клик по кнопке Elements
        elements_button = BaseComponent(self.driver, (By.XPATH, "//h5[text()='Elements']"))
        elements_button.click()

        # Проверка URL (дополнительная проверка)
        assert self.driver.current_url == 'https://demoqa.com/elements'

        # Создание компонента для текста по центру
        center_text = BaseComponent(self.driver, (By.CSS_SELECTOR, ".col-12.mt-4.col-md-6"))

        # Проверка текста
        expected_text = "Please select an item from left to start practice."
        actual_text = center_text.get_text()

        assert actual_text == expected_text, f"Ожидался текст: '{expected_text}', получен: '{actual_text}'"