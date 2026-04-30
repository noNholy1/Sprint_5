import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from urls import MAIN_PAGE


class TestFromPersonalAccountToConstructor:
    
    def test_return_via_constructor_button(self, driver, login):
        # Переходим в личный кабинет
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        
        # Ждем загрузки ЛК
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.PROFILE_SECTION)
        )
        
        # Возвращаемся через кнопку Конструктор
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR_HEADER).click()
        
        # Проверяем возврат на главную
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        
        # Дополнительные проверки
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER).is_displayed()
        assert driver.current_url == MAIN_PAGE
        
    def test_return_via_logo(self, driver, login):
        # Переходим в личный кабинет
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        
        # Ждем загрузки ЛК
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.PROFILE_SECTION)
        )
        
        # Возвращаемся через логотип
        driver.find_element(*TestLocators.LOGO).click()
        
        # Проверяем возврат на главную
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        
        # Дополнительные проверки
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER).is_displayed()
        assert driver.current_url == MAIN_PAGE