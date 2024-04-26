import time

from locators import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from user_account import UserAccount


class TestRegistrationUser:
    def test_registration_form_positive_test(self, web_drv, email, password):
        UserAccount.registration_user(web_drv, 'Владимир', email, password)
        wait = WDWait(web_drv, 10)
        wait.until(ec.element_to_be_clickable(LINK_PERSONAL_ACCOUNT_IN_HEADER)).click()
        UserAccount.login_user(web_drv, email, password)
        time.sleep(2)
        wait.until(ec.element_to_be_clickable(LINK_PERSONAL_ACCOUNT_IN_HEADER)).click()
        assert wait.until(ec.visibility_of_element_located(
            INPUT_FIELD_LOGIN_IN_PERSONAL_ACCOUNT)).get_attribute('value') == email

    def test_registration_with_incorrect_password(self, web_drv, email):
        UserAccount.registration_user(web_drv, 'Владимир', email, '12345')
        assert web_drv.find_element(*ERROR_MESSAGE_INCORRECT_PASSWORD_IN_REG_FORM)
