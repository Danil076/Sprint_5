import pytest
import random
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()

# Функция для генерации почты и пароля
@pytest.fixture(scope="function")
def users():
    random_digits = random.randint(100, 999)

    domain = random.choice(["yandex.ru", "gmail.com"])

    email = f"danil_klimov_55_{random_digits}@{domain}"

    password = "password" + str(random.randint(10, 99))

    return {"email": email, "password": password}