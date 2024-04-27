import pytest

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from user_account import UserAccount
from locators import (LoginPageLocator as LogPL,
                      HeaderLocator as HeadL,
                      RegisterPageLocator as RegPL,
                      ForgotPasswordPageLocator as FPassPL,
                      MainPageLocator as MainPL,
                      AccountProfilePageLocator as AccPPL)
from config import URL


class TestPersonalAccount:
    def test_login_by_login_button_on_main_page(self, web_drv, login_details):
        """
            Проверка входа в аккаунт по кнопке "Войти в аккаунт" на главной странице.
            :param web_drv: WebDriver
            :param login_details: статичные данные (email, пароль)
            :return: None
        """
        web_drv.find_element(*LogPL.BUTTON_LOGIN).click()
        assert UserAccount.check_email_in_new_account(web_drv, *login_details) == login_details[0]

    def test_login_by_personal_account_button_on_header(self, web_drv, login_details):
        """
            Проверка входа в аккаунт по кнопке "Личный кабинет" в шапке сайта.
            :param web_drv: WebDriver
            :param login_details: статичные данные (email, пароль)
            :return: None
        """
        web_drv.find_element(*HeadL.LINK_PERSONAL_ACCOUNT).click()
        assert UserAccount.check_email_in_new_account(web_drv, *login_details) == login_details[0]

    def test_login_by_button_in_registration_form(self, web_drv, login_details):
        """
            Проверка входа в аккаунт по кнопке "Войти" в форме регистрации.
            :param web_drv: WebDriver
            :param login_details: статичные данные (email, пароль)
            :return: None
        """
        web_drv.get(f'{URL}/register')
        web_drv.find_element(*RegPL.LINK_LOGIN).click()
        assert UserAccount.check_email_in_new_account(web_drv, *login_details) == login_details[0]

    def test_login_by_button_in_password_recovery_form(self, web_drv, login_details):
        """
            Проверка входа в аккаунт по кнопке "Войти" в форме восстановления пароля.
            :param web_drv: WebDriver
            :param login_details: статичные данные (email, пароль)
            :return: None
        """
        web_drv.get(f'{URL}/forgot-password')
        web_drv.find_element(*FPassPL.LINK_LOGIN).click()
        assert UserAccount.check_email_in_new_account(web_drv, *login_details) == login_details[0]

    @pytest.mark.parametrize(
        'locator',
        (HeadL.LINK_CONSTRUCTOR, HeadL.LOGO)
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
        web_drv.get(f'{URL}/login')
        UserAccount.login_user(web_drv, *login_details)
        web_drv.find_element(*HeadL.LINK_PERSONAL_ACCOUNT).click()
        web_drv.find_element(*locator).click()
        assert web_drv.find_element(*MainPL.HEADER_ASSEMBLE_BURGER).is_displayed()

    # Выход по кнопке «Выйти» в личном кабинете
    def test_exit_by_logout_button_personal_account(self, web_drv, login_details):
        """
            Проверка выхода из аккаунта по кнопке "Выйти" в личном кабинете
            :param web_drv: WebDriver
            :param login_details: статичные данные (email, пароль)
            :return: None
        """
        web_drv.get(f'{URL}/login')
        UserAccount.login_user(web_drv, *login_details)
        wait = WDWait(web_drv, 10)
        wait.until(ec.element_to_be_clickable(HeadL.LINK_PERSONAL_ACCOUNT)).click()
        wait.until(ec.element_to_be_clickable(AccPPL.BUTTON_EXIT)).click()
        wait.until(ec.element_to_be_clickable(HeadL.LINK_PERSONAL_ACCOUNT)).click()
        assert wait.until(ec.visibility_of_element_located(LogPL.HEADER_ENTER)).is_displayed()
