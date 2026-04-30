import sys
import os
# Добавляем текущую директорию в путь поиска модулей
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pytest
from selenium import webdriver
from urls import MAIN_PAGE

@pytest.fixture(scope='function')
def driver():
    # Настройка опций Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)
    driver.get(MAIN_PAGE)
    
    yield driver
    # Закрытие драйвера после теста
    driver.quit()

@pytest.fixture
def login(driver):
    from helpers import go_to_login_form, fill_login_credentials, submit_login, wait_for_successful_login
    
    go_to_login_form(driver)
    fill_login_credentials(driver)
    submit_login(driver)
    wait_for_successful_login(driver)