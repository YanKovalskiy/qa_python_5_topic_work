from selenium.webdriver.common.by import By


class HeaderLocator:
    # Ссылка на Личный кабинет в шапке сайте
    LINK_PERSONAL_ACCOUNT = By.XPATH, "//header/nav/a"

    # Ссылка на Конструктор в шапке сайте
    LINK_CONSTRUCTOR = By.XPATH, "//header/nav/ul/li[1]/a"

    # Логотип в шапке сайта
    LOGO = By.XPATH, "//header/nav/div/a"


class MainPageLocator:
    # Заголовок на главной странице "Соберите бургер"
    HEADER_ASSEMBLE_BURGER = By.TAG_NAME, 'h1'

    # Кнопка «Войти в аккаунт» на главной странице
    BUTTON_LOGIN = By.XPATH, "//button[text()='Войти в аккаунт']"

    # Вкладка "Булки" в конструкторе бургеров
    TAB_BUNS = By.XPATH, "//span[text()='Булки']/parent::div"

    # Вкладка "Соусы" в конструкторе бургеров
    TAB_SAUCES = By.XPATH, "//span[text()='Соусы']/parent::div"

    # Вкладка "Булки" в конструкторе бургеров
    TAB_FILLINGS = By.XPATH, "//span[text()='Начинки']/parent::div"

    # Модальное окно ожидания загрузки
    MODAL_WAIT_WINDOW = By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']"


class LoginPageLocator:
    # Поле вода Email в форме аутентификации при входе в Личный кабинет
    INPUT_FIELD_EMAIL = By.XPATH, "//input[@type='text']"

    # Поле вода Пароль в форме аутентификации при входе в Личный кабинет
    INPUT_FIELD_PASSWORD = By.XPATH, "//input[@type='password']"

    # Кнопка "Войти" в форме аутентификации при входе в Личный кабинет
    BUTTON_LOGIN = By.XPATH, "//button[text()='Войти']"

    # Ссылка "Зарегистрироваться" в форме аутентификации при входе в Личный кабинет
    LINK_REGISTER = By.LINK_TEXT, 'Зарегистрироваться'

    # Ссылка "Восстановить пароль" в форме аутентификации при входе в Личный кабинет
    LINK_RECOVERY_PASSWORD = By.LINK_TEXT, 'Восстановить пароль'

    # Заголовок в форме аутентификации при входе в Личный кабинет
    HEADER_ENTER = By.XPATH, "//h2[text()='Вход']"


class AccountProfilePageLocator:
    # Поле ввода Логин в Личном кабинете
    INPUT_FIELD_LOGIN = By.XPATH, "//input[@name='name' and @type='text']"

    # Кнопка Выход в Личном кабинете
    BUTTON_EXIT = By.XPATH, "//button[text()='Выход']"


class RegisterPageLocator:
    # Поле вода Имя в форме регистрации
    INPUT_FIELD_NAME = By.XPATH, "//label[text()='Имя']//parent::div/input"

    # Поле вода Email в форме регистрации
    INPUT_FIELD_EMAIL = By.XPATH, "//label[text()='Email']//parent::div/input"

    # Поле вода Пароль в форме регистрации
    INPUT_FIELD_PASSWORD = By.NAME, 'Пароль'

    # Кнопка "Зарегистрироваться" в форме регистрации
    BUTTON_REGISTER = By.XPATH, "//button[text()='Зарегистрироваться']"

    # Ссылка "Войти" в форме регистрации
    LINK_LOGIN = By.LINK_TEXT, "Войти"

    # Сообщение об ошибке "Некорректный пароль"
    ERROR_MESSAGE_INCORRECT_PASSWORD = By.XPATH, "//p[text()='Некорректный пароль']"


class ForgotPasswordPageLocator:
    # Ссылка "Войти" в форме Восстановление пароля
    LINK_LOGIN = By.LINK_TEXT, "Войти"
