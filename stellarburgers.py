from locators import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait


def registration_user(web_drv, user_name, email, password):
    WDWait(web_drv, 3).until(ec.element_to_be_clickable(LINK_PERSONAL_ACCOUNT_IN_HEADER))

    web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()

    WDWait(web_drv, 3).until(ec.element_to_be_clickable(LINK_REGISTER_IN_LOGIN_FORM))

    web_drv.find_element(*LINK_REGISTER_IN_LOGIN_FORM).click()

    WDWait(web_drv, 3).until(ec.element_to_be_clickable(BUTTON_REGISTER_IN_REG_FORM))

    web_drv.find_element(*INPUT_FIELD_NAME_IN_REG_FORM).send_keys(user_name)
    web_drv.find_element(*INPUT_FIELD_EMAIL_IN_REG_FORM).send_keys(email)
    web_drv.find_element(*INPUT_FIELD_PASSWORD_IN_REG_FORM).send_keys(password)
    web_drv.find_element(*BUTTON_REGISTER_IN_REG_FORM).click()


def login_user(web_drv, email, password):
    WDWait(web_drv, 3).until(ec.element_to_be_clickable(BUTTON_LOGIN_IN_LOGIN_FORM))
    web_drv.find_element(*INPUT_FIELD_EMAIL_IN_LOGIN_FORM).send_keys(email)
    web_drv.find_element(*INPUT_FIELD_PASSWORD_IN_LOGIN_FORM).send_keys(password)
    web_drv.find_element(*BUTTON_LOGIN_IN_LOGIN_FORM).click()


def get_email_from_account(web_drv):
    WDWait(web_drv, 3).until(ec.element_to_be_clickable(LINK_PERSONAL_ACCOUNT_IN_HEADER))
    web_drv.find_element(*LINK_PERSONAL_ACCOUNT_IN_HEADER).click()
    WDWait(web_drv, 3).until(ec.visibility_of_element_located(INPUT_FIELD_LOGIN_IN_PERSONAL_ACCOUNT))
    return web_drv.find_element(*INPUT_FIELD_LOGIN_IN_PERSONAL_ACCOUNT).get_attribute('value')


def check_email_in_new_account(web_drv, email, password):
    login_user(web_drv, email, password)
    return get_email_from_account(web_drv)
