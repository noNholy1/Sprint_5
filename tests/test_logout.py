import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators


class TestLogout:
    def test_logout_from_personal_account(self, driver, logged_in_user):
        # Переход в личный кабинет
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        # Ожидание загрузки страницы профиля (как пример, можно проверить наличие кнопки «Выход»)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGOUT))
        # Клик по кнопке «Выход»
        driver.find_element(*TestLocators.BUTTON_LOGOUT).click()
        # Проверка, что после выхода отображается кнопка «Войти»
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN))