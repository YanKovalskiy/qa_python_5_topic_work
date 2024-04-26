import pytest

from locators import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from user_account import UserAccount


class TestPersonalAccount:
    def test_login_by_login_button_on_main_page(self, web_drv, login_details):
        """
            Проверка входа в аккаунт по кнопке "Войти в аккаунт" на главной странице.
            :param web_drv: WebDriver
            :param login_details: статичные данные (email, пароль)
            :return: None
        """
        web_drv.find_element(*BUTTON_LOGIN_ON_MAIN_PAGE).click()
        assert UserAccount.check_email_in_new_account(web_drv, *login_details) == login_details[0]

    def test_login_by_personal_account_button_on_header(self, web_drv, login_details):
        """
            Проверка входа в аккаунт по кнопке "Личный кабинет" в шапке сайта.
            :param web_drv: WebDriver
            :param login_details: статичные данные (email, пароль)
            :return: None
        """
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        assert UserAccount.check_email_in_new_account(web_drv, *login_details) == login_details[0]

    def test_login_by_button_in_registration_form(self, web_drv, login_details):
        """
            Проверка входа в аккаунт по кнопке "Войти" в форме регистрации.
            :param web_drv: WebDriver
            :param login_details: статичные данные (email, пароль)
            :return: None
        """
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        web_drv.find_element(*LINK_REGISTER_IN_LOGIN_FORM).click()
        web_drv.find_element(*LINK_LOGIN_IN_REG_FORM).click()
        assert UserAccount.check_email_in_new_account(web_drv, *login_details) == login_details[0]

    def test_login_by_button_in_password_recovery_form(self, web_drv, login_details):
        """
            Проверка входа в аккаунт по кнопке "Войти" в форме восстановления пароля.
            :param web_drv: WebDriver
            :param login_details: статичные данные (email, пароль)
            :return: None
        """
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        web_drv.find_element(*LINK_RECOVERY_PASSWORD_IN_LOGIN_FORM).click()
        web_drv.find_element(*LINK_LOGIN_IN_RECOVERY_PASS_FORM).click()
        assert UserAccount.check_email_in_new_account(web_drv, *login_details) == login_details[0]

    @pytest.mark.parametrize(
        'locator',
        (LINK_CONSTRUCTOR_IN_HEADER, LOGO_IN_HEADER)
    )
    def test_following_link_from_personal_account(self, web_drv, login_details, locator):
        """
            Проверка перехода из личного кабинета в конструктор по клику на:
            - кнопку "Конструктор"
            - логотип Stellar Burgers
            :param web_drv: WebDriver
            :param login_details: статичные данные (email, пароль)
            :param locator: целевой локатор
            :return: None
        """
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        UserAccount.login_user(web_drv, *login_details)
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        web_drv.find_element(*locator).click()
        assert web_drv.find_element(*HEADER_ON_MAIN_PAGE)

    # Выход по кнопке «Выйти» в личном кабинете
    def test_exit_by_logout_button_personal_account(self, web_drv, login_details):
        """
            Проверка выхода из аккаунта по кнопке "Выйти" в личном кабинете
            :param web_drv: WebDriver
            :param login_details: статичные данные (email, пароль)
            :return: None
        """
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        UserAccount.login_user(web_drv, *login_details)
        wait = WDWait(web_drv, 10)
        wait.until(ec.element_to_be_clickable(LINK_PERSONAL_ACCOUNT_IN_HEADER)).click()
        wait.until(ec.element_to_be_clickable(BUTTON_EXIT_IN_PERSONAL_ACCOUNT)).click()
        assert wait.until(ec.visibility_of_element_located(HEADER_ON_LOGIN_FORM))
