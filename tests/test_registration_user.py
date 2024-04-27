from user_account import UserAccount
from locators import *
from config import URL


class TestRegistrationUser:
    def test_registration_form_positive_test(self, web_drv, email, password):
        """
            Регистрация пользователя позитивный сценарий:
            - «Имя» должно быть не пустым
            - в поле Email введён email в формате логин@домен: например, 123@ya.ru
            - минимальный пароль — шесть символов
            :param web_drv: WebDriver
            :param email: сгенерированный email
            :param password: сгенерированный пароль
            :return: None
        """
        UserAccount.registration_user(web_drv, 'Владимир', email, password)
        web_drv.get(f'{URL}/login')
        assert UserAccount.check_email_in_new_account(web_drv, email, password) == email

    def test_registration_with_incorrect_password(self, web_drv, email):
        """
            Регистрация пользователя негативный сценарий:
            - некорректный пароль, менее 6 символов
            :param web_drv: WebDriver
            :param email: сгенерированный email
            :return: None
            """
        UserAccount.registration_user(web_drv, 'Владимир', email, '12345')
        assert web_drv.find_element(*ERROR_MESSAGE_INCORRECT_PASSWORD_IN_REG_FORM).is_displayed()
