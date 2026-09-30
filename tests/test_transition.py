import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTransitions:
    # Тест 1: Переход в личный кабинет авторизованного пользователя
    def test_go_to_personal_account(self, driver):
        # Открываем страницу логина
        driver.get(Data.STELLAR_BURGER_LOGIN)

        # Авторизуемся (вводим email и пароль)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.VALID_USER_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.VALID_USER_PASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждем перехода на главную страницу (успешный вход)
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_MAIN))

        # Кликаем на ссылку "Личный кабинет" в шапке
        driver.find_element(*Locators.LINK_ACCOUNT_HEADER).click()

        # Ждем, пока в URL появится слово "account"
        WebDriverWait(driver, 10).until(EC.url_contains("account"))

        # Проверяем, что мы в личном кабинете
        assert driver.current_url == Data.STELLAR_BURGER_ACCOUNT


    # Тест 2: Переход из личного кабинета в конструктор
    def test_go_to_constructor_from_account(self, driver):
        # Открываем главную страницу
        driver.get(Data.STELLAR_BURGER_MAIN)

        # Кликаем на "Личный кабинет"
        driver.find_element(*Locators.LINK_ACCOUNT_HEADER).click()

        # Ждем перехода на страницу логина
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_LOGIN))

        # Кликаем на ссылку "Конструктор" в шапке
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()

        # Ждем возврата на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_MAIN))

        # Проверяем, что мы на главной
        assert driver.current_url == Data.STELLAR_BURGER_MAIN


    # Тест 3: Переход на главную через логотип
    def test_go_to_logo(self, driver):
        # Открываем главную страницу
        driver.get(Data.STELLAR_BURGER_MAIN)

        # Кликаем на "Личный кабинет"
        driver.find_element(*Locators.LINK_ACCOUNT_HEADER).click()

        # Ждем перехода на страницу логина
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_LOGIN))

        # Кликаем на логотип Stellar Burgers
        driver.find_element(*Locators.LOGO).click()

        # Ждем возврата на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_MAIN))

        # Проверяем, что мы на главной
        assert driver.current_url == Data.STELLAR_BURGER_MAIN


    # Тест 4: Выход из аккаунта
    def test_logout_from_account(self, driver):
        # Открываем страницу логина
        driver.get(Data.STELLAR_BURGER_LOGIN)

        # Авторизуемся
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.VALID_USER_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.VALID_USER_PASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_MAIN))

        # Кликаем на "Личный кабинет"
        driver.find_element(*Locators.LINK_ACCOUNT_HEADER).click()

        # Ждем перехода в личный кабинет
        WebDriverWait(driver, 10).until(EC.url_contains("account"))

        # Ждем, пока кнопка "Выход" станет кликабельной, и кликаем на неё
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUTTON_LOGOUT)
        )
        logout_button.click()

        # Ждем перехода на страницу логина (после выхода)
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_LOGIN))

        # Проверяем, что мы на странице логина
        assert driver.current_url == Data.STELLAR_BURGER_LOGIN
