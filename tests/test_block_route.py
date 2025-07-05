import allure
from url import TestUrl
from pages.route_page import RoutePage
from locators.route_page_locators import RoutePageLocators
from locators.block_route_locators import BlockRouteLocators
from pages.block_route_page import BlockRoute
from data import Data
from helpers import Helpers

class TestBlockRoute:

    @allure.title('Проверка появления блока с выбором маршрута')
    def test_block_route(self, driver):
        route = Helpers()
        route.route(driver)
        block_route = BlockRoute(driver)
        class_name = block_route.find_block_route()
        assert class_name.get_attribute('class') == 'type-picker shown'

    @allure.title('Проверка ввода одинакового адреса в поля Откуда и Куда')
    def test_same_from_to_text_and_duration(self, driver):
        route_page = RoutePage(driver)
        route_page.go_to_url(TestUrl.HOMEPAGE_URL)
        route_page.enter_field_from(Data.FIRST_ADDRESS)
        route_page.enter_field_to(Data.FIRST_ADDRESS)
        route_page.find_element_with_wait(RoutePageLocators.A_AND_B_LOCATORS)
        block_route = BlockRoute(driver)
        text = block_route.route_result_price()
        duration = block_route.route_result_duration()
        assert text == "Авто Бесплатно" and duration == "В пути 0 мин."

    @allure.title('Проверка смены активного таба и пересчета времени и стоимости')
    def test_change_active_mode(self, driver):
        route = Helpers()
        route.route(driver)
        block_route = BlockRoute(driver)
        old_price = block_route.route_result_price()
        old_duration = block_route.route_result_duration()
        block_route.click_mode_tab(BlockRouteLocators.LOCATOR_OPTIMAL_MODE)
        new_tab= block_route.get_active_mode_tab()
        new_price = block_route.route_result_price()
        new_duration = block_route.route_result_duration()
        assert new_tab == "Оптимальный" and old_price != new_price and old_duration != new_duration

    @allure.title('Проверка переключения на таб Свой')
    def test_mode_svoy(self,driver):
        route = Helpers()
        route.route(driver)
        block_route = BlockRoute(driver)
        block_route.click_mode_tab(BlockRouteLocators.LOCATOR_SVOY_MODE)
        new_tab = block_route.get_active_mode_tab()
        disabled_modes = block_route.find_types(BlockRouteLocators.LOCATOR_TYPES_DISABLED)
        assert new_tab == "Свой" and len(disabled_modes) == 0

    @allure.title('Проверка видимости кнопки Вызвать такси')
    def test_visibility_order_taxi_button(self, driver):
        route = Helpers()
        route.route(driver)
        block_route = BlockRoute(driver)
        block_route.click_mode_tab(BlockRouteLocators.LOCATOR_SVOY_MODE)
        block_route.click_mode_tab(BlockRouteLocators.LOCATOR_FAST_MODE)
        assert block_route.find_element_with_wait(BlockRouteLocators.BUTTON_ORDER_TAXI).is_displayed() == True

    @allure.title('Проверка видимости кнопки Забронировать')
    def test_visibility_book_taxi_button(self, driver):
        route = Helpers()
        route.route(driver)
        block_route = BlockRoute(driver)
        block_route.click_mode_tab(BlockRouteLocators.LOCATOR_SVOY_MODE)
        block_route.click_to_element(BlockRouteLocators.SVOY_MODE_DRIVE_TYPE)
        assert block_route.find_element_with_wait(BlockRouteLocators.BUTTON_BOOK_TAXI).is_displayed() == True