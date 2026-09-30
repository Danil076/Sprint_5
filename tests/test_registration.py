from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
    #Тест на успешную регистрацию
    def test_registration_success(self,driver,users):
        # Открываем страницу регистрации
        driver.get(Data.STELLAR_BURGER_REGISTER)

        # Заполняем форму регистрации (имя, email, пароль)
        driver.find_element(*Locators.INPUT_NAME).send_keys(Data.USER_NAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(users["email"])
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(users["password"])

        # Кликаем на кнопку "Зарегистрироваться"
        driver.find_element(*Locators.BUTTON_REGISTER).click()

        # Ждем перехода на страницу логина (успешная регистрация)
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.STELLAR_BURGER_LOGIN))

        # Ждем перехода на страницу логина (успешная регистрация)
        assert driver.current_url == Data.STELLAR_BURGER_LOGIN


    # Тест 2: Ошибка при регистрации с коротким паролем (меньше 6 символов)
    def test_error_short_password(self, driver, users):
        # Открываем страницу регистрации
        driver.get(Data.STELLAR_BURGER_REGISTER)

        # Заполняем форму, но пароль вводим короткий ("123")
        driver.find_element(*Locators.INPUT_NAME).send_keys(Data.USER_NAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(users["email"])
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys("123")

        # Кликаем на кнопку "Зарегистрироваться"
        driver.find_element(*Locators.BUTTON_REGISTER).click()

        # Ждем появления блока с ошибкой (красная рамка вокруг поля пароля)
        error_block = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.ERROR_PASSWORD)
        )

        # Проверяем, что блок ошибки виден на экране
        assert error_block.is_displayed()
    