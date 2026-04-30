import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import TestUser


# Функции генерации тестовых данных
def generate_random_email():
    random_digits = random.randint(100, 999)
    return f'nikita_chikunov_41_123{random_digits}@yandex.ru'

def generate_random_password():
    length = random.randint(8, 12)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_name():
    names = ['Anna', 'Milena', 'Madonna', 'Elena', 'Oleg']
    surnames = ['Ganbarov', 'Ivanova', 'Bolkonski', 'Mironov', 'Popova']
    return f'{random.choice(names)} {random.choice(surnames)}'


# Функции авторизации
def go_to_login_form(driver):
    driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
    )

def fill_login_credentials(driver):
    driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(TestUser.EXISTING_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(TestUser.EXISTING_PASSWORD)

def submit_login(driver):
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()

def wait_for_successful_login(driver):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
    )


# Функции работы с конструктором
def switch_section(driver, section_locator, expected_section):
    driver.find_element(*section_locator).click()
    wait_for_section_active(driver, expected_section)
    assert driver.find_element(*TestLocators.ACTIVE_SECTION).text == expected_section

def wait_for_section_active(driver, section_name):
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(TestLocators.ACTIVE_SECTION, section_name)
    )


# Функции регистрации
def fill_registration_form(driver, name, email, password):
    driver.find_element(*TestLocators.INPUT_NAME).send_keys(name)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_SUBMIT).click()

def go_to_registration_form(driver):
    driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
    )
    driver.find_element(*TestLocators.BUTTON_REGISTER).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
    )


# Универсальные вспомогательные функции
def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def click_element(driver, locator):
    element = wait_for_element(driver, locator)
    element.click()