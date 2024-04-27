from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from locators import (HeaderLocator as HeadPL,
                      RegisterPageLocator as RegPL,
                      LoginPageLocator as LogPL,
                      AccountProfilePageLocator as AccPPL)
from config import URL


class UserAccount:
    @staticmethod
    def registration_user(web_drv, user_name, email, password):
        web_drv.get(f'{URL}/register')
        reg_button = WDWait(web_drv, 10).until(ec.element_to_be_clickable(RegPL.BUTTON_REGISTER))
        web_drv.find_element(*RegPL.INPUT_FIELD_NAME).send_keys(user_name)
        web_drv.find_element(*RegPL.INPUT_FIELD_EMAIL).send_keys(email)
        web_drv.find_element(*RegPL.INPUT_FIELD_PASSWORD).send_keys(password)
        reg_button.click()

    @staticmethod
    def login_user(web_drv, email, password):
        wait = WDWait(web_drv, 10)
        wait.until(ec.element_to_be_clickable(LogPL.INPUT_FIELD_EMAIL)).send_keys(email)
        wait.until(ec.element_to_be_clickable(LogPL.INPUT_FIELD_PASSWORD)).send_keys(password)
        wait.until(ec.element_to_be_clickable(LogPL.BUTTON_LOGIN)).click()

    @staticmethod
    def get_email_from_account(web_drv):
        WDWait(web_drv, 10).until(ec.element_to_be_clickable(HeadPL.LINK_PERSONAL_ACCOUNT)).click()
        email = WDWait(web_drv, 10).until(ec.visibility_of_element_located(
            AccPPL.INPUT_FIELD_LOGIN)).get_attribute('value')
        return email

    @staticmethod
    def check_email_in_new_account(web_drv, email, password):
        UserAccount.login_user(web_drv, email, password)
        return UserAccount.get_email_from_account(web_drv)
