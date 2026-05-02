import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from helpers import generate_random_email, generate_random_password, generate_name
from data import TestUser


class TestRegistration:
    
    def test_registration_new_account_success_submit(self, driver):
        random_email = generate_random_email()
        random_password = generate_random_password()
        random_name = generate_name()
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(random_name)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN)
        )
        assert driver.find_element(*TestLocators.BUTTON_REGISTER).is_displayed()

    def test_registration_name_is_empty_submit(self, driver):
        random_email = generate_random_email()
        random_password = generate_random_password()
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys('')
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed()

    def test_registration_invalid_email_no_at_symbol(self, driver):
        random_password = generate_random_password()
        invalid_email = "invalidemail.example.com"
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestUser.EXISTING_NAME)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(invalid_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed()

    def test_registration_email_no_domain(self, driver):
        random_password = generate_random_password()
        invalid_email = "test@example."
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestUser.EXISTING_NAME)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(invalid_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed()

    @pytest.mark.parametrize('valid_password', ['123456', '1234567', '123456789012'])
    def test_registration_valid_length_password_submit(self, driver, valid_password):
        random_email = generate_random_email()
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestUser.EXISTING_NAME)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(valid_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN)
        )
        assert driver.find_element(*TestLocators.BUTTON_REGISTER).is_displayed()

    @pytest.mark.parametrize('wrong_password', ['12345', '1234', '1', ''])
    def test_registration_invalid_length_password_submit(self, driver, wrong_password):
        random_email = generate_random_email()
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestUser.EXISTING_NAME)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(wrong_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed()

    @pytest.mark.parametrize('wrong_password', ['12345', '1234', '1'])
    def test_registration_short_password_error(self, driver, wrong_password):
        random_email = generate_random_email()
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestUser.EXISTING_NAME)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(wrong_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        assert driver.find_element(*TestLocators.NOTIFICATION_INCORRECT_PASSWORD).is_displayed()
        
    def test_registration_existing_user_failed(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestUser.EXISTING_NAME)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(TestUser.EXISTING_EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(TestUser.EXISTING_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed()