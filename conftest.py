import pytest
import random
import string


from selenium import webdriver
from config import URL


@pytest.fixture()
def web_drv():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    yield driver

    driver.quit()


@pytest.fixture()
def email():
    return f'vladimir_yankovskiy_8_{random.randint(1000, 9999)}@gmail.com'


@pytest.fixture()
def password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(7))


@pytest.fixture()
def login_details():
    return 'yankovskiy_8@gmail.com', '123456'
