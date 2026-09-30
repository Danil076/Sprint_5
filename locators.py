from selenium.webdriver.common.by import By 

class Locators:

    # Локаторы формы регистрации
    INPUT_NAME = (By.XPATH, "//label[text() = 'Имя']/../input")  # Поле "Имя" в форме регистрации
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input")  # Поле "Email" в форме регистрации
    INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")  # Поле "Пароль" в форме регистрации
    BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    ERROR_PASSWORD = (By.XPATH, "//div[contains(@class, 'input_status_error')]")  # Блок ошибки при невалидном пароле

    # === Кнопки и ссылки навигации ===
    BUTTON_LOGIN_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной странице
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти" на странице логина
    LINK_ACCOUNT_HEADER = (By.XPATH, "//a[contains(@href, '/account')]")  # Ссылка "Личный кабинет" в шапке сайта
    BUTTON_LOG_IN = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти" на страницах регистрации и восстановления пароля
    LINK_FORGOT_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка "Восстановить пароль"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//a[.//p[text()='Конструктор']]")  # Ссылка "Конструктор" в шапке сайта
    LOGO = (By.XPATH, "//a[@href='/']")  # Логотип Stellar Burgers (ведет на главную)
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход" в личном кабинете

    # === Вкладки конструктора ===
    TAB_BUNS = (By.XPATH, "//span[text()='Булки']")  # Вкладка "Булки" в конструкторе
    TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']")  # Вкладка "Соусы" в конструкторе
    TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']")  # Вкладка "Начинки" в конструкторе

    # === Ингредиенты для клика (проверка работы разделов) ===
    INGREDIENT_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")  # Изображение булки в разделе "Булки"
    INGREDIENT_SAUCE = (By.XPATH, "//img[@alt='Соус с шипами Антарианского плоскоходца']")  # Изображение соуса в разделе "Соусы"
    INGREDIENT_FILLING = (By.XPATH, "//img[@alt='Сыр с астероидной плесенью']")  # Изображение начинки в разделе "Начинки"

    # === Заголовки в модальном окне (проверка корректности открытия) ===
    MODAL_TITLE_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")  # Заголовок модального окна для булки
    MODAL_TITLE_SAUCE = (By.XPATH, "//p[text()='Соус с шипами Антарианского плоскоходца']")  # Заголовок модального окна для соуса
    MODAL_TITLE_FILLING = (By.XPATH, "//p[text()='Сыр с астероидной плесенью']")  # Заголовок модального окна для начинки
    