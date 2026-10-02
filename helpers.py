import random

def generate_user_data():
    #Генерирует уникальные тестовые данные для регистрации
    random_digits = random.randint(100, 999)
    domain = random.choice(["yandex.ru", "gmail.com"])
    email = f"danil_klimov_55_{random_digits}@{domain}"
    password = "password" + str(random.randint(10, 99))
    return {"email": email, "password": password}