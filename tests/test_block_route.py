import allure
from pages.route_page import RoutePage
from pages.block_route_page import BlockRoute
from data import Data

class TestBlockRoute:

    @allure.title('Проверка появления блока с выбором маршрута')
    def test_block_route(self, driver):
        route_page = RoutePage(driver)
        route_page.enter_route(Data.FIRST_ADDRESS, Data.SECOND_ADDRESS)
        block_route = BlockRoute(driver)
        class_name = block_route.find_block_route()
        assert class_name.get_attribute('class') == 'type-picker shown'

    @allure.title('Проверка ввода одинакового адреса в поля Откуда и Куда')
    def test_same_from_to_text_and_duration(self, driver):
        route_page = RoutePage(driver)
        route_page.enter_route(Data.FIRST_ADDRESS, Data.FIRST_ADDRESS)
        block_route = BlockRoute(driver)
        text = block_route.route_result_price()
        duration = block_route.route_result_duration()
        assert text == Data.CHECK_SAME_ADDRESS_TEXT and duration == Data.CHECK_SAME_ADDRESS_DURATION

    @allure.title('Проверка смены активного таба с Быстрого на Оптимальный и пересчета времени и стоимости')
    def test_switch_tab(self, driver):
        route_page = RoutePage(driver)
        route_page.enter_route(Data.FIRST_ADDRESS, Data.SECOND_ADDRESS)
        block_route = BlockRoute(driver)
        old_price = block_route.route_result_price()
        old_duration = block_route.route_result_duration()
        block_route.click_optimal_mode_tab()
        new_tab= block_route.get_active_mode_tab()
        new_price = block_route.route_result_price()
        new_duration = block_route.route_result_duration()
        assert new_tab == Data.NAME_OPTIMAL_TAB and old_price != new_price and old_duration != new_duration

    @allure.title('Проверка переключения на таб Свой')
    def test_mode_svoy(self,driver):
        route_page = RoutePage(driver)
        route_page.enter_route(Data.FIRST_ADDRESS, Data.SECOND_ADDRESS)
        block_route = BlockRoute(driver)
        block_route.click_svoy_mode_tab()
        new_tab = block_route.get_active_mode_tab()
        disabled_modes = block_route.find_types()
        assert new_tab == Data.NAME_SVOY_TAB and len(disabled_modes) == 0

    @allure.title('Проверка видимости кнопки Вызвать такси')
    def test_visibility_order_taxi_button(self, driver):
        route_page = RoutePage(driver)
        route_page.enter_route(Data.FIRST_ADDRESS, Data.SECOND_ADDRESS)
        block_route = BlockRoute(driver)
        block_route.click_svoy_mode_tab()
        block_route.click_fast_mode_tab()
        assert block_route.check_visibility_button_order_taxi() == True

    @allure.title('Проверка видимости кнопки Забронировать')
    def test_visibility_book_taxi_button(self, driver):
        route_page = RoutePage(driver)
        route_page.enter_route(Data.FIRST_ADDRESS, Data.SECOND_ADDRESS)
        block_route = BlockRoute(driver)
        block_route.click_svoy_mode_tab()
        block_route.click_svoy_mode_drive_type()
        assert block_route.check_visibility_button_book_taxi() == True