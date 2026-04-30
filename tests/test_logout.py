import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators


class TestLogout:
    
    def test_logout_of_personal_account(self, driver, login):
        # Проверяем, что авторизованы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        
        # Переходим в личный кабинет
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        
        # Ждем загрузки личного кабинета
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.PROFILE_SECTION)
        )
        
        # Выходим из системы
        driver.find_element(*TestLocators.BUTTON_LOGOUT).click()
        
        # Проверяем, что вернулись на страницу авторизации
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN)
        )
        
        # Дополнительные проверки
        assert driver.find_element(*TestLocators.BUTTON_LOGIN).is_displayed()
        assert '/login' in driver.current_url