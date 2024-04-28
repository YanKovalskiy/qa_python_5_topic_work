import pytest

from locators import MainPageLocator as MainPL


class TestConstructor:
    @pytest.mark.parametrize(
        'tab_locator',
        (
            (MainPL.TAB_FILLINGS, MainPL.TAB_SAUCES)
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
        web_drv.find_element(*MainPL.TAB_SAUCES).click()
        tab_buns = web_drv.find_element(*MainPL.TAB_BUNS)
        tab_buns.click()
        assert 'type_current' in tab_buns.get_attribute('class')
