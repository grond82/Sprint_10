import pytest
import allure
from pages.tariffs_page import TariffPage
from locators.tariffs_page_locators import TariffsPageLocators
from pages.block_route_page import BlockRoute
from data import Data
from helpers import Helpers

class TestTariffPage:

    @allure.title('Проверка тарифов')
    def test_open_tariffs_page(self, driver):
        route = Helpers()
        route.route(driver)
        block_route = BlockRoute(driver)
        block_route.click_order_taxi_button()
        tariff_page = TariffPage(driver)
        active_tariff = tariff_page.find_element_with_wait(TariffsPageLocators.TARIFF_WORK_ACTIVE)
        tariffs_name_on_page = tariff_page.get_tariffs_name_on_page()
        assert tariffs_name_on_page == Data.TARIFFS_NAME and active_tariff.get_attribute('class') == 'tcard active'

    @allure.title('Проверка блока опций под тарифами')
    def test_visibility_tariff_options(self, driver):
        route = Helpers()
        route.route(driver)
        block_route = BlockRoute(driver)
        block_route.click_order_taxi_button()
        tariff_page = TariffPage(driver)
        result = tariff_page.check_block_tariff_options()
        assert result == True

    @allure.title('Проверка всплывающего окна с описанием тарифа')
    @pytest.mark.xfail(reason = "Баг с перепутанным описанием тарифов Сонный и Разговорчивый")
    @pytest.mark.parametrize(
        "tariff_name, tariff_description",
        [
            ('Рабочий', 'Для деловых особ, которых отвлекают'),
            ('Сонный', 'Для тех, кто не выспался'),
            ('Отпускной', 'Если пришла пора отдохнуть'),
            ('Разговорчивый', 'Если мысли не выходят из головы'),
            ('Утешительный', 'Если хочется свернуться калачиком'),
            ('Глянцевый', 'Если нужно блистать')
        ]
    )
    def test_tariffs(self, driver, tariff_name, tariff_description):
        route = Helpers()
        route.route(driver)
        block_route = BlockRoute(driver)
        block_route.click_order_taxi_button()
        tariff_page = TariffPage(driver)
        tariff_page.click_tariffs(tariff_name)
        tariff_page.hover_mouse_tariff_info()
        tariff_name_active, tariff_name_info, tariff_description_info = tariff_page.get_name_tariff_active_and_info()
        assert tariff_name_active == tariff_name and tariff_name_info == tariff_name and tariff_description_info == tariff_description