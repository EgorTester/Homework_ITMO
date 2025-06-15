from pages.swag_labs import SwagLabs

def test_check_icon_exist(driver):
    """Тест проверки наличия иконки на странице"""
    swag_labs_page = SwagLabs(driver)
    swag_labs_page.visit()
    assert swag_labs_page.exist_icon()

def test_check_username_field_exist(driver):
    """Тест проверки наличия поля имени пользователя"""
    swag_labs_page = SwagLabs(driver)
    swag_labs_page.visit()
    assert swag_labs_page.exist_username_field()

def test_check_password_field_exist(driver):
    """Тест проверки наличия поля пароля"""
    swag_labs_page = SwagLabs(driver)
    swag_labs_page.visit()
    assert swag_labs_page.exist_password_field()