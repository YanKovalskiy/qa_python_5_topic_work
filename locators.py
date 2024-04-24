from selenium.webdriver.common.by import By

# ------------------------------------------------------------------------------
#  main page
# ------------------------------------------------------------------------------

# Ссылка на Личный кабинет в шапке сайте
LINK_PERSONAL_ACCOUNT_IN_HEADER = By.XPATH, ".//header/nav/a"

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

# ------------------------------------------------------------------------------
#  /account/profile
# ------------------------------------------------------------------------------

# Поле ввода Логин в Личном кабинете
INPUT_FIELD_LOGIN_IN_PERSONAL_ACCOUNT = By.XPATH, ".//li[2]/div/div/input"

# ------------------------------------------------------------------------------
#  /register
# ------------------------------------------------------------------------------

# Поле вода Имя в форме регистрации
INPUT_FIELD_NAME_IN_REG_FORM = By.XPATH, ".//fieldset[1]/div/div/input"

# Поле вода Email в форме регистрации
INPUT_FIELD_EMAIL_IN_REG_FORM = By.XPATH, ".//fieldset[2]/div/div/input"

# Поле вода Пароль в форме регистрации
INPUT_FIELD_PASSWORD_IN_REG_FORM = By.NAME, 'Пароль'

# Кнопка Зарегистрироваться в форме регистрации
BUTTON_REGISTER_IN_REG_FORM = By.XPATH, ".//button[text()='Зарегистрироваться']"

# Сообщение об ошибке "Некорректный пароль"
ERROR_MESSAGE_INCORRECT_PASSWORD_IN_REG_FORM = By.XPATH, ".//p[text()='Некорректный пароль']"
