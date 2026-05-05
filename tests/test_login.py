import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from data import TestUser
from helpers import fill_login_credentials, submit_login, wait_for_successful_login


class TestLogin:
    
    def test_login_via_main_login_button(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        
        fill_login_credentials(driver)
        submit_login(driver)
        wait_for_successful_login(driver)
        
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER).is_displayed()

    def test_login_via_personal_account_button(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        
        fill_login_credentials(driver)
        submit_login(driver)
        wait_for_successful_login(driver)
        
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER).is_displayed()

    def test_login_via_registration_form(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_REG_FORM).click()
        
        fill_login_credentials(driver)
        submit_login(driver)
        wait_for_successful_login(driver)
        
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER).is_displayed()
        
    def test_login_via_password_recovery_form(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        
        driver.find_element(*TestLocators.BUTTON_FORGOT_PASSWORD).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_PASSWORD_RECOVERY)
        )
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_PASSWORD_RECOVERY).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        
        fill_login_credentials(driver)
        submit_login(driver)
        wait_for_successful_login(driver)
        
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER).is_displayed()