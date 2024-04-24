import stellarburgers as sb

from locators import *


class TestPersonalAccount:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_by_login_button_on_main_page(self, web_drv, email, password):
        web_drv.find_element(*BUTTON_LOGIN_ON_MAIN_PAGE).click()
        assert sb.check_email_in_new_account(web_drv, 'Владимир',email, password) == email

    # Вход через кнопку «Личный кабинет»
    def test_login_personal_account_button_on_header(self, web_drv, email, password):
        web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
        assert sb.check_email_in_new_account(web_drv, 'Владимир',email, password) == email