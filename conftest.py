import pytest
from selenium import webdriver
from helpers import generate_user_data


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()

# Функция для генерации почты и пароля
@pytest.fixture(scope="function")
def users():
    return generate_user_data()
