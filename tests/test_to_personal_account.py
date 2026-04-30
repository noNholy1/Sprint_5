import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators


class TestToPersonalAccount:
    
    def test_go_to_personal_account(self, driver, login):
        # Переходим в личный кабинет
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        
        # Ждем загрузки и проверяем элементы ЛК
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.PROFILE_SECTION)
        )
        
        # Проверяем, что оба раздела отображаются
        assert driver.find_element(*TestLocators.PROFILE_SECTION).is_displayed()
        assert driver.find_element(*TestLocators.ORDER_HISTORY_SECTION).is_displayed()