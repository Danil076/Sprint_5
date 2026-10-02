import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    # Тест 1: Вход через кнопку "Войти в аккаунт" на главной странице
    def test_login_from_main_page(self, driver):
        # Открываем главную страницу
        driver.get(Data.STELLAR_BURGER_MAIN)

        # Кликаем на кнопку "Войти в аккаунт"
        driver.find_element(*Locators.BUTTON_LOGIN_MAIN).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(Data.STELLAR_BURGER_LOGIN))

        # Вводим email и пароль зарегистрированного пользователя
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.VALID_USER_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.VALID_USER_PASSWORD)

        # Вводим email и пароль зарегистрированного пользователя
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждем возврата на главную страницу (успешный вход)
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_MAIN))

        # Проверяем, что мы действительно на главной
        assert driver.current_url == Data.STELLAR_BURGER_MAIN
    

    # Тест 2: Вход через ссылку "Личный кабинет" в шапке сайта
    def test_login_from_header_link(self, driver):

        driver.get(Data.STELLAR_BURGER_MAIN)

        # Кликаем на ссылку "Личный кабинет" (нас перекинет на страницу логина)
        driver.find_element(*Locators.LINK_ACCOUNT_HEADER).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_LOGIN))

        # Вводим данные для входа
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.VALID_USER_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.VALID_USER_PASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждем возврата на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_MAIN))

        # Проверяем, что мы на главной
        assert driver.current_url == Data.STELLAR_BURGER_MAIN

    
    # Тест 3: Вход через ссылку "Войти" на странице регистрации
    def test_login_from_register_page(self, driver):
        # Открываем страницу регистрации
        driver.get(Data.STELLAR_BURGER_REGISTER)

        # Кликаем на ссылку "Войти" (переходим на страницу логина)
        driver.find_element(*Locators.BUTTON_LOG_IN).click()

        # Ждем перехода на страницу логина
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_LOGIN))

        # Вводим данные для входа
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.VALID_USER_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.VALID_USER_PASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждем возврата на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_MAIN))

        # Проверяем, что мы на главной
        assert driver.current_url == Data.STELLAR_BURGER_MAIN


    # Тест 4: Вход через ссылку "Войти" на странице восстановления пароля
    def test_login_from_forgot_password_page(self, driver):
        # Открываем страницу восстановления пароля
        driver.get(Data.STELLAR_BURGER_FORGOT_PASSWORD)

        # Кликаем на ссылку "Войти" (переходим на страницу логина)
        driver.find_element(*Locators.BUTTON_LOG_IN).click()

        # Ждем перехода на страницу логина
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_LOGIN))

        # Ждем перехода на страницу логина
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.VALID_USER_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.VALID_USER_PASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
      
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_MAIN))

        # Проверяем, что мы на главной        
        assert driver.current_url == Data.STELLAR_BURGER_MAIN
