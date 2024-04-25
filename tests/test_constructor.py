import pytest

from locators import *


class TestConstructor:

    # Раздел Конструктор. Переходы к разделу «Начинки»
    def test_tab_fillings_in_constructor(self, web_drv):
        web_drv.find_element(*TAB_FILLINGS_IN_CONSTRUCTOR).click()
        assert web_drv.find_element(*TITLE_SECTION_FILLINGS_IN_CONSTRUCTOR)

    # Раздел Конструктор. Переходы к разделам: «Булки», «Соусы»
    @pytest.mark.parametrize(
        'test_locator,target_locator',
        (
            (TAB_SAUCES_IN_CONSTRUCTOR, TITLE_SECTION_SAUCES_IN_CONSTRUCTOR),
            (TAB_BUNS_IN_CONSTRUCTOR, TITLE_SECTION_BUNS_IN_CONSTRUCTOR),
        )
    )
    def test_tabs_buns_and_sauces_in_constructor(self, web_drv, test_locator, target_locator):
        web_drv.find_element(*TAB_FILLINGS_IN_CONSTRUCTOR).click()
        web_drv.find_element(*test_locator).click()
        assert web_drv.find_element(*target_locator)