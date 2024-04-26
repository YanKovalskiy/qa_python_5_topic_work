import pytest

from locators import *


class TestConstructor:
    def test_tab_fillings_in_constructor(self, web_drv):
        """
            Раздел Конструктор. Проверка перехода к разделу «Начинки».
            :param web_drv: WebDriver
            :return: None
        """
        web_drv.find_element(*TAB_FILLINGS_IN_CONSTRUCTOR).click()
        assert web_drv.find_element(*TITLE_SECTION_FILLINGS_IN_CONSTRUCTOR)

    # Раздел Конструктор. Переходы к разделам:
    @pytest.mark.parametrize(
        'test_locator,target_locator',
        (
            (TAB_SAUCES_IN_CONSTRUCTOR, TITLE_SECTION_SAUCES_IN_CONSTRUCTOR),
            (TAB_BUNS_IN_CONSTRUCTOR, TITLE_SECTION_BUNS_IN_CONSTRUCTOR),
        )
    )
    def test_tabs_buns_and_sauces_in_constructor(self, web_drv, test_locator, target_locator):
        """
            Раздел Конструктор. Проверка перехода к разделам:
            - "Булки"
            - "Соусы"
            :param web_drv: WebDriver
            :param test_locator: тестируемый локатор
            :param target_locator: локатор для верификации
            :return: None
        """
        web_drv.find_element(*TAB_FILLINGS_IN_CONSTRUCTOR).click()
        web_drv.find_element(*test_locator).click()
        assert web_drv.find_element(*target_locator)
