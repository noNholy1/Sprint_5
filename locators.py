from selenium.webdriver.common.by import By


class TestLocators:
     # регистрация
    INPUT_NAME = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
    INPUT_EMAIL = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    INPUT_PASSWORD = (By.NAME, "Пароль")
    BUTTON_SUBMIT = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    NOTIFICATION_INCORRECT_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")
    
    # авторизация
    BUTTON_LOGIN_MAIN = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    LOGIN_IN_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    INPUT_EMAIL_AUTH = (By.NAME, "name")
    INPUT_PASSWORD_AUTH = (By.NAME, "Пароль")
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(),'Войти')]")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
    # ссылки и переходы
    BUTTON_LOGIN_IN_REG_FORM = (By.XPATH, "//a[contains(text(),'Войти')]")
    BUTTON_REGISTER = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    LOGIN_IN = (By.XPATH, "//a[text()='Войти']")
    
    # восстановление пароля
    BUTTON_FORGOT_PASSWORD = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    BUTTON_LOGIN_PASSWORD_RECOVERY = (By.XPATH, "//a[contains(text(),'Войти')]")
    
    # личный кабинет 
    PROFILE_SECTION = (By.XPATH, "//a[contains(@href,'/account/profile')]")
    ORDER_HISTORY_SECTION = (By.XPATH, "//a[contains(@href,'/account/order-history')]")
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(),'Выход')]")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # главная страница 
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    BUTTON_CONSTRUCTOR_HEADER = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    LOGO_XPATH = (By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']")
    
    # конструктор
    SECTION_BUNS = (By.XPATH, "//span[contains(text(),'Булки')]")
    SECTION_SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]")
    SECTION_FILLINGS = (By.XPATH, "//span[contains(text(),'Начинки')]")
    BUNS = (By.XPATH, "//span[text()='Булки']")
    SAUCES = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_SECTION = (By.CLASS_NAME, "tab_tab_type_current__2BEPc")
    
    # текстовые элементы 
    TEXT_BUNS = (By.XPATH, "//h2[text()='Булки']")
    TEXT_SAUCES = (By.XPATH, "//h2[text()='Соусы']")
    TEXT_FILLINGS = (By.XPATH, "//h2[text()='Начинки']")
    
    # поля ввода (альтернативные локаторы) 
    NAME = (By.XPATH, "//label[text()='Имя']/parent::div/input")
    EMAIL = (By.XPATH, "//label[text()='Email']/parent::div/input")
    PASSWORD = (By.XPATH, "//input[@type='password']")