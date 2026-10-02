import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConstructor:
    # проверка раздела "Булки"
    def test_buns_section(self, driver):
        driver.get(Data.STELLAR_BURGER_MAIN)

        #кликаем на "Соусы" (уходим с булок)
        driver.find_element(*Locators.TAB_SAUCES).click()

        #кликаем обратно на "Булки" (проверяем, что кнопка работает)
        driver.find_element(*Locators.TAB_BUNS).click()

        # Ждем, пока вкладка "Булки" станет активной (появится класс tab_tab_type_current)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.TAB_BUNS_ACTIVE)
        )

        # Проверяем, что активная вкладка действительно "Булки"
        assert driver.find_element(*Locators.TAB_BUNS_ACTIVE).is_displayed()

    # проверка раздела "Соусы"
    def test_sauces_section(self, driver):
        driver.get(Data.STELLAR_BURGER_MAIN)

        #кликаем на "Соусы"
        driver.find_element(*Locators.TAB_SAUCES).click()

        # Ждем, пока вкладка "Соусы" станет активной
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.TAB_SAUCES_ACTIVE)
        )

        # Проверяем, что активная вкладка действительно "Соусы"
        assert driver.find_element(*Locators.TAB_SAUCES_ACTIVE).is_displayed()

    # проверка раздела "Начинки"
    def test_fillings_section(self, driver):
        driver.get(Data.STELLAR_BURGER_MAIN)

        #кликаем на "Начинки"
        driver.find_element(*Locators.TAB_FILLINGS).click()

        # Ждем, пока вкладка "Начинки" станет активной
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.TAB_FILLINGS_ACTIVE)
        )

        # Проверяем, что активная вкладка действительно "Начинки"
        assert driver.find_element(*Locators.TAB_FILLINGS_ACTIVE).is_displayed()
        