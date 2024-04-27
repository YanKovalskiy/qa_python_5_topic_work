import pytest

from locators import *


class TestConstructor:
    @pytest.mark.parametrize(
        'tab_locator',
        (
            (TAB_FILLINGS_IN_CONSTRUCTOR, TAB_SAUCES_IN_CONSTRUCTOR)
        )
    )
    def test_tabs_in_constructor(self, web_drv, tab_locator):
        """
            Раздел Конструктор. Проверка перехода к разделам:
            - "Соусы"
            - "Начинки"
            :param web_drv: WebDriver
            :param tab_locator: тестируемый локатор
            :return: None
        """
        tab = web_drv.find_element(*tab_locator)
        tab.click()
        assert 'type_current' in tab.get_attribute('class')

    def test_tab_buns_in_constructor(self, web_drv):
        """
            Раздел Конструктор. Проверка перехода к разделу "Булки"
            :param web_drv: WebDriver
            :return: None
        """
        web_drv.find_element(*TAB_SAUCES_IN_CONSTRUCTOR).click()
        tab = web_drv.find_element(*TAB_BUNS_IN_CONSTRUCTOR)
        tab.click()
        assert 'type_current' in tab.get_attribute('class')
