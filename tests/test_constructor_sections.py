import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import SectionData
from helpers import click_section_tab


class TestConstructorSections:

    def test_initial_section_is_buns(self, driver):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_MAIN)
        )
        assert driver.find_element(*TestLocators.ACTIVE_SECTION).text == SectionData.NAMES["buns"]
        
    def test_switch_to_buns_section_is_active(self, driver, logged_in_user):
        click_section_tab(driver, TestLocators.SECTION_BUNS)
        assert WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(TestLocators.ACTIVE_SECTION, SectionData.NAMES["buns"])
        )

    def test_switch_to_sauces_section_is_active(self, driver, logged_in_user):
        click_section_tab(driver, TestLocators.SECTION_SAUCES)
        assert WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(TestLocators.ACTIVE_SECTION, SectionData.NAMES["sauces"])
        )

    def test_switch_to_fillings_section_is_active(self, driver, logged_in_user):
        click_section_tab(driver, TestLocators.SECTION_FILLINGS)
        assert WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(TestLocators.ACTIVE_SECTION, SectionData.NAMES["fillings"])
        )
    def test_buns_content_displayed(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_MAIN))
        assert driver.find_element(*TestLocators.TEXT_BUNS).is_displayed()

    def test_sauces_content_displayed(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_MAIN))
        driver.find_element(*TestLocators.SECTION_SAUCES).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.TEXT_SAUCES))
        assert driver.find_element(*TestLocators.TEXT_SAUCES).is_displayed()

    def test_fillings_content_displayed(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_MAIN))
        driver.find_element(*TestLocators.SECTION_FILLINGS).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.TEXT_FILLINGS))
        assert driver.find_element(*TestLocators.TEXT_FILLINGS).is_displayed()