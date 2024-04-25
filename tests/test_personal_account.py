import pytest
import stellarburgers as sb

from locators import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait


class TestPersonalAccount:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_by_login_button_on_main_page(self, web_drv, login_details):
        web_drv.find_element(*BUTTON_LOGIN_ON_MAIN_PAGE).click()
        assert sb.check_email_in_new_account(web_drv, *login_details) == login_details[0]

    # Вход через кнопку «Личный кабинет»
    def test_login_by_personal_account_button_on_header(self, web_drv, login_details):
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        assert sb.check_email_in_new_account(web_drv, *login_details) == login_details[0]

    # Вход через кнопку в форме регистрации
    def test_login_by_button_in_registration_form(self, web_drv, login_details):
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        web_drv.find_element(*LINK_REGISTER_IN_LOGIN_FORM).click()
        web_drv.find_element(*LINK_LOGIN_IN_REG_FORM).click()
        assert sb.check_email_in_new_account(web_drv, *login_details) == login_details[0]

    # Вход через кнопку в форме восстановления пароля
    def test_login_by_button_in_password_recovery_form(self, web_drv, login_details):
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        web_drv.find_element(*LINK_RECOVERY_PASSWORD_IN_LOGIN_FORM).click()
        web_drv.find_element(*LINK_LOGIN_IN_RECOVERY_PASS_FORM).click()
        assert sb.check_email_in_new_account(web_drv, *login_details) == login_details[0]

    @pytest.mark.parametrize(
        'locator',
        (LINK_CONSTRUCTOR_IN_HEADER, LOGO_IN_HEADER)
    )
    # Переход из личного кабинета в конструктор по клику на «Конструктор» и логотип Stellar Burgers
    def test_following_link_from_personal_account(self, web_drv, login_details, locator):
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        sb.login_user(web_drv, *login_details)
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        web_drv.find_element(*locator).click()
        assert web_drv.find_element(*HEADER_ON_MAIN_PAGE)

    # Выход по кнопке «Выйти» в личном кабинете
    def test_exit_by_logout_button_personal_account(self, web_drv, login_details):
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        sb.login_user(web_drv, *login_details)
        wait = WDWait(web_drv, 10)
        wait.until(ec.element_to_be_clickable(LINK_PERSONAL_ACCOUNT_IN_HEADER)).click()
        wait.until(ec.element_to_be_clickable(BUTTON_EXIT_IN_PERSONAL_ACCOUNT)).click()
        assert wait.until(ec.visibility_of_element_located(HEADER_ON_LOGIN_FORM))
