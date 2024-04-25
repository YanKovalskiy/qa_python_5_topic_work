import time

import stellarburgers as sb
from locators import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait


class TestRegistrationUser:
    def test_registration_form_positive_test(self, web_drv, email, password):
        sb.registration_user(web_drv, 'Владимир', email, password)
        WDWait(web_drv, 10).until(ec.element_to_be_clickable(LINK_PERSONAL_ACCOUNT_IN_HEADER)).click()
        sb.login_user(web_drv, email, password)
        time.sleep(2)
        WDWait(web_drv, 10).until(ec.element_to_be_clickable(LINK_PERSONAL_ACCOUNT_IN_HEADER)).click()
        filed_email = WDWait(web_drv, 10).until(ec.visibility_of_element_located(INPUT_FIELD_LOGIN_IN_PERSONAL_ACCOUNT))
        assert filed_email.get_attribute('value') == email

    def test_registration_with_incorrect_password(self, web_drv, email):
        sb.registration_user(web_drv, 'Владимир', email, '12345')
        assert web_drv.find_element(*ERROR_MESSAGE_INCORRECT_PASSWORD_IN_REG_FORM)
