import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from urls import MAIN_PAGE


class TestFromPersonalAccountToConstructor:
    
    def test_navigate_to_constructor_via_constructor_button(self, driver, logged_in_user):
        # Переход в личный кабинет
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGOUT)
        )
        # Клик по кнопке «Конструктор»
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR_HEADER).click()
        # Проверка, что появилась кнопка «Оформить заказ»
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER))

    def test_navigate_to_constructor_via_logo(self, driver, logged_in_user):
        # Переход в личный кабинет
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGOUT)
        )
        # Клик по логотипу
        driver.find_element(*TestLocators.LOGO).click()
        # Проверка, что появилась кнопка «Оформить заказ»
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER))