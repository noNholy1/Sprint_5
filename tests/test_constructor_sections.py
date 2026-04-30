import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import SectionData
from helpers import switch_section, wait_for_section_active


class TestConstructorSections:

    def test_initial_section_is_buns(self, driver):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_MAIN)
        )
        assert driver.find_element(*TestLocators.ACTIVE_SECTION).text == SectionData.NAMES["buns"]

    @pytest.mark.parametrize("section_locator,expected_section", [
        (TestLocators.SECTION_SAUCES, SectionData.NAMES["sauces"]),
        (TestLocators.SECTION_FILLINGS, SectionData.NAMES["fillings"])
    ])
    def test_switch_from_buns(self, driver, section_locator, expected_section):
        switch_section(driver, section_locator, expected_section)

    @pytest.mark.parametrize("from_section,to_section,expected_section", [
        (TestLocators.SECTION_SAUCES, TestLocators.SECTION_BUNS, SectionData.NAMES["buns"]),
        (TestLocators.SECTION_SAUCES, TestLocators.SECTION_FILLINGS, SectionData.NAMES["fillings"]),
        (TestLocators.SECTION_FILLINGS, TestLocators.SECTION_BUNS, SectionData.NAMES["buns"]),
        (TestLocators.SECTION_FILLINGS, TestLocators.SECTION_SAUCES, SectionData.NAMES["sauces"])
    ])
    def test_switch_between_sections(self, driver, from_section, to_section, expected_section):
        # Сначала переходим в исходный раздел
        driver.find_element(*from_section).click()
        wait_for_section_active(driver, 
            SectionData.NAMES["sauces"] if from_section == TestLocators.SECTION_SAUCES 
            else SectionData.NAMES["fillings"]
        )
        
        # Затем переходим в целевой раздел
        switch_section(driver, to_section, expected_section)

    def test_sections_with_login(self, driver, login):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        
        # Проверяем все переходы после логина
        switch_section(driver, TestLocators.SECTION_SAUCES, TestLocators.TEXT_SAUCES)
        switch_section(driver, TestLocators.SECTION_FILLINGS, TestLocators.TEXT_FILLINGS)
        switch_section(driver, TestLocators.SECTION_BUNS, TestLocators.TEXT_BUNS)

    def test_section_content_changes(self, driver):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_MAIN)
        )
        
        # Булки - Соусы
        assert driver.find_element(*TestLocators.TEXT_BUNS).is_displayed()
        switch_section(driver, TestLocators.SECTION_SAUCES, SectionData.NAMES["sauces"])
        assert driver.find_element(*TestLocators.TEXT_SAUCES).is_displayed()
        
        # Соусы - Начинки
        switch_section(driver, TestLocators.SECTION_FILLINGS, SectionData.NAMES["fillings"])
        assert driver.find_element(*TestLocators.TEXT_FILLINGS).is_displayed()