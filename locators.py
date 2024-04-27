from selenium.webdriver.common.by import By

# ------------------------------------------------------------------------------
#  header
# ------------------------------------------------------------------------------

# Ссылка на Личный кабинет в шапке сайте
LINK_PERSONAL_ACCOUNT_IN_HEADER = By.XPATH, "//header/nav/a"

# Ссылка на Конструктор в шапке сайте
LINK_CONSTRUCTOR_IN_HEADER = By.XPATH, "//header/nav/ul/li[1]/a"

# Логотип в шапке сайта
LOGO_IN_HEADER = By.XPATH, "//header/nav/div/a"

# ------------------------------------------------------------------------------
#  main page
# ------------------------------------------------------------------------------

# Заголовок на главной странице "Соберите бургер"
HEADER_ON_MAIN_PAGE = By.TAG_NAME, 'h1'

# Кнопка «Войти в аккаунт» на главной странице
BUTTON_LOGIN_ON_MAIN_PAGE = By.XPATH, "//button[text()='Войти в аккаунт']"

# Вкладка "Булки" в конструкторе бургеров
TAB_BUNS_IN_CONSTRUCTOR = By.XPATH, "//span[text()='Булки']/parent::div"

# Вкладка "Соусы" в конструкторе бургеров
TAB_SAUCES_IN_CONSTRUCTOR = By.XPATH, "//span[text()='Соусы']/parent::div"

# Вкладка "Булки" в конструкторе бургеров
TAB_FILLINGS_IN_CONSTRUCTOR = By.XPATH, "//span[text()='Начинки']/parent::div"

# Заголовок раздела "Булки" в конструкторе бургеров
TITLE_SECTION_BUNS_IN_CONSTRUCTOR = By.XPATH, "//h2[text()='Булки']"

# Заголовок раздела "Соусы" в конструкторе бургеров
TITLE_SECTION_SAUCES_IN_CONSTRUCTOR = By.XPATH, "//h2[text()='Соусы']"

# Заголовок раздела "Начинки" в конструкторе бургеров
TITLE_SECTION_FILLINGS_IN_CONSTRUCTOR = By.XPATH, "//h2[text()='Начинки']"

# ------------------------------------------------------------------------------
#  /login
# ------------------------------------------------------------------------------

# Поле вода Email в форме аутентификации при входе в Личный кабинет
INPUT_FIELD_EMAIL_IN_LOGIN_FORM = By.XPATH, "//input[@type='text']"

# Поле вода Пароль в форме аутентификации при входе в Личный кабинет
INPUT_FIELD_PASSWORD_IN_LOGIN_FORM = By.XPATH, "//input[@type='password']"

# Кнопка "Войти" в форме аутентификации при входе в Личный кабинет
BUTTON_LOGIN_IN_LOGIN_FORM = By.XPATH, "//button[text()='Войти']"

# Ссылка "Зарегистрироваться" в форме аутентификации при входе в Личный кабинет
LINK_REGISTER_IN_LOGIN_FORM = By.LINK_TEXT, 'Зарегистрироваться'

# Ссылка "Восстановить пароль" в форме аутентификации при входе в Личный кабинет
LINK_RECOVERY_PASSWORD_IN_LOGIN_FORM = By.LINK_TEXT, 'Восстановить пароль'

# Заголовок в форме аутентификации при входе в Личный кабинет
HEADER_ON_LOGIN_FORM = By.XPATH, "//h2[text()='Вход']"

# ------------------------------------------------------------------------------
#  /account/profile
# ------------------------------------------------------------------------------

# Поле ввода Логин в Личном кабинете
INPUT_FIELD_LOGIN_IN_PERSONAL_ACCOUNT = By.XPATH, "//input[@name='name' and @type='text']"

# Кнопка Выход в Личном кабинете
BUTTON_EXIT_IN_PERSONAL_ACCOUNT = By.XPATH, "//button[text()='Выход']"

# ------------------------------------------------------------------------------
#  /register
# ------------------------------------------------------------------------------

# Поле вода Имя в форме регистрации
INPUT_FIELD_NAME_IN_REG_FORM = By.XPATH, "//label[text()='Имя']//parent::div/input"

# Поле вода Email в форме регистрации
INPUT_FIELD_EMAIL_IN_REG_FORM = By.XPATH, "//label[text()='Email']//parent::div/input"

# Поле вода Пароль в форме регистрации
INPUT_FIELD_PASSWORD_IN_REG_FORM = By.NAME, 'Пароль'

# Кнопка "Зарегистрироваться" в форме регистрации
BUTTON_REGISTER_IN_REG_FORM = By.XPATH, "//button[text()='Зарегистрироваться']"

# Ссылка "Войти" в форме регистрации
LINK_LOGIN_IN_REG_FORM = By.LINK_TEXT, "Войти"

# Сообщение об ошибке "Некорректный пароль"
ERROR_MESSAGE_INCORRECT_PASSWORD_IN_REG_FORM = By.XPATH, "//p[text()='Некорректный пароль']"

# ------------------------------------------------------------------------------
#  /forgot-password
# ------------------------------------------------------------------------------
# Ссылка "Войти" в форме Восстановление пароля
LINK_LOGIN_IN_RECOVERY_PASS_FORM = By.LINK_TEXT, "Войти"
