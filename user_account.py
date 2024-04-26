from locators import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait


class UserAccount:
    @staticmethod
    def registration_user(web_drv, user_name, email, password):
        wait = WDWait(web_drv, 10)
        wait.until(ec.element_to_be_clickable(LINK_PERSONAL_ACCOUNT_IN_HEADER)).click()
        wait.until(ec.element_to_be_clickable(LINK_REGISTER_IN_LOGIN_FORM)).click()
        web_drv.find_element(*INPUT_FIELD_NAME_IN_REG_FORM).send_keys(user_name)
        web_drv.find_element(*INPUT_FIELD_EMAIL_IN_REG_FORM).send_keys(email)
        web_drv.find_element(*INPUT_FIELD_PASSWORD_IN_REG_FORM).send_keys(password)
        wait.until(ec.element_to_be_clickable(BUTTON_REGISTER_IN_REG_FORM)).click()

    @staticmethod
    def login_user(web_drv, email, password):
        web_drv.find_element(*INPUT_FIELD_EMAIL_IN_LOGIN_FORM).send_keys(email)
        web_drv.find_element(*INPUT_FIELD_PASSWORD_IN_LOGIN_FORM).send_keys(password)
        WDWait(web_drv, 10).until(ec.element_to_be_clickable(BUTTON_LOGIN_IN_LOGIN_FORM)).click()

    @staticmethod
    def get_email_from_account(web_drv):
        wait = WDWait(web_drv, 10)
        wait.until(ec.element_to_be_clickable(LINK_PERSONAL_ACCOUNT_IN_HEADER)).click()
        return wait.until(ec.visibility_of_element_located(
            INPUT_FIELD_LOGIN_IN_PERSONAL_ACCOUNT)).get_attribute('value')

    @staticmethod
    def check_email_in_new_account(web_drv, email, password):
        UserAccount.login_user(web_drv, email, password)
        return UserAccount.get_email_from_account(web_drv)
