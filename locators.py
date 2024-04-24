from selenium.webdriver.common.by import By

# ------------------------------------------------------------------------------
#  main page
# ------------------------------------------------------------------------------

# Ссылка на Личный кабинет в шапке сайте
LINK_PERSONAL_ACCOUNT_IN_HEADER = By.XPATH, ".//header/nav/a"

# Заголовок на главной странице "Соберите бургер"
HEADER_ON_MAIN_PAGE = By.TAG_NAME, 'h1'

# Ссылка на Конструктор в шапке сайте
LINK_CONSTRUCTOR_IN_HEADER = By.XPATH, ".//header/nav/ul/li[1]/a"

# Логотип в шапке сайта
LOGO_IN_HEADER = By.XPATH, ".//header/nav/div/a"

# Кнопка «Войти в аккаунт» на главной странице
BUTTON_LOGIN_ON_MAIN_PAGE = By.XPATH, ".//button[text()='Войти в аккаунт']"

# ------------------------------------------------------------------------------
#  /login
# ------------------------------------------------------------------------------

# Поле вода Email в форме аутентификации при входе в Личный кабинет
INPUT_FIELD_EMAIL_IN_LOGIN_FORM = By.XPATH, ".//fieldset[1]/div/div/input"

# Поле вода Пароль в форме аутентификации при входе в Личный кабинет
INPUT_FIELD_PASSWORD_IN_LOGIN_FORM = By.XPATH, ".//fieldset[2]/div/div/input"

# Кнопка "Войти" в форме аутентификации при входе в Личный кабинет
BUTTON_LOGIN_IN_LOGIN_FORM = By.XPATH, ".//button[text()='Войти']"

# Ссылка "Зарегистрироваться" в форме аутентификации при входе в Личный кабинет
LINK_REGISTER_IN_LOGIN_FORM = By.LINK_TEXT, 'Зарегистрироваться'

# Ссылка "Восстановить пароль" в форме аутентификации при входе в Личный кабинет
LINK_RECOVERY_PASSWORD_IN_LOGIN_FORM = By.LINK_TEXT, 'Восстановить пароль'

# Заголовок в форме аутентификации при входе в Личный кабинет
HEADER_ON_LOGIN_FORM = By.XPATH, ".//main/div/h2"

# ------------------------------------------------------------------------------
#  /account/profile
# ------------------------------------------------------------------------------

# Поле ввода Логин в Личном кабинете
INPUT_FIELD_LOGIN_IN_PERSONAL_ACCOUNT = By.XPATH, ".//li[2]/div/div/input"

# Кнопка Выход в Личном кабинете
BUTTON_EXIT_IN_PERSONAL_ACCOUNT = By.XPATH, ".//nav/ul/li[3]/button"

# ------------------------------------------------------------------------------
#  /register
# ------------------------------------------------------------------------------

# Поле вода Имя в форме регистрации
INPUT_FIELD_NAME_IN_REG_FORM = By.XPATH, ".//fieldset[1]/div/div/input"

# Поле вода Email в форме регистрации
INPUT_FIELD_EMAIL_IN_REG_FORM = By.XPATH, ".//fieldset[2]/div/div/input"

# Поле вода Пароль в форме регистрации
INPUT_FIELD_PASSWORD_IN_REG_FORM = By.NAME, 'Пароль'

# Кнопка "Зарегистрироваться" в форме регистрации
BUTTON_REGISTER_IN_REG_FORM = By.XPATH, ".//button[text()='Зарегистрироваться']"

# Ссылка "Войти" в форме регистрации
LINK_LOGIN_IN_REG_FORM = By.LINK_TEXT, "Войти"  # By.XPATH, ".//a[text()='Войти']"

# Сообщение об ошибке "Некорректный пароль"
ERROR_MESSAGE_INCORRECT_PASSWORD_IN_REG_FORM = By.XPATH, ".//p[text()='Некорректный пароль']"

# ------------------------------------------------------------------------------
#  /forgot-password
# ------------------------------------------------------------------------------
# Ссылка "Войти" в форме Восстановление пароля
LINK_LOGIN_IN_RECOVERY_PASS_FORM = By.LINK_TEXT, "Войти"
