import pytest
import random
import string


from selenium import webdriver


@pytest.fixture()
def web_drv():

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    # Initialize Firefox/Gecko WebDriver
    # driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site/')

    yield driver

    driver.quit()


@pytest.fixture()
def email():
    return f'vladimir_yankovskiy_8_{random.randint(100, 999)}@gmail.com'


@pytest.fixture()
def password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(6))
