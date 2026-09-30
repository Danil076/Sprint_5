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

        #кликаем на булку
        driver.find_element(*Locators.INGREDIENT_BUN).click()

        #проверяем модальное окно
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MODAL_TITLE_BUN)
        )

        assert driver.find_element(*Locators.MODAL_TITLE_BUN).is_displayed()

    # проверка раздела "Соусы"
    def test_sauces_section(self, driver):
        driver.get(Data.STELLAR_BURGER_MAIN)

        #кликаем на "Соусы"
        driver.find_element(*Locators.TAB_SAUCES).click()

        #кликаем на соус
        driver.find_element(*Locators.INGREDIENT_SAUCE).click()

        #проверяем модальное окно
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MODAL_TITLE_SAUCE)
        )
        assert driver.find_element(*Locators.MODAL_TITLE_SAUCE).is_displayed()

    # проверка раздела "Начинки"
    def test_fillings_section(self, driver):
        driver.get(Data.STELLAR_BURGER_MAIN)

        #кликаем на "Начинки"
        driver.find_element(*Locators.TAB_FILLINGS).click()

        #кликаем на начинку
        driver.find_element(*Locators.INGREDIENT_FILLING).click()

        #проверяем модальное окно
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MODAL_TITLE_FILLING)
        )

        assert driver.find_element(*Locators.MODAL_TITLE_FILLING).is_displayed()
