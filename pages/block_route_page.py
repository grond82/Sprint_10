import allure
from locators.block_route_locators import BlockRouteLocators
from pages.base_page import BasePage

class BlockRoute(BasePage):

    @allure.step('Найти блок маршрута')
    def find_block_route(self):
        return self.find_element_with_wait(BlockRouteLocators.BLOCK_ROUTE)

    @allure.step('Получить цену')
    def route_result_price(self):
        return self.get_text_from_element(BlockRouteLocators.LOCATOR_PRICE)

    @allure.step('Получить время в пути')
    def route_result_duration(self):
        return self.get_text_from_element(BlockRouteLocators.LOCATOR_DURATION)

    @allure.step('Получить активный таб видов маршрута')
    def get_active_mode_tab(self):
        return self.get_text_from_element(BlockRouteLocators.LOCATOR_ACTIVE_MODE)

    @allure.step('Кликнуть на таб Оптимальный')
    def click_optimal_mode_tab(self):
        self.click_to_element(BlockRouteLocators.LOCATOR_OPTIMAL_MODE)

    @allure.step('Кликнуть на таб Свой')
    def click_svoy_mode_tab(self):
        self.click_to_element(BlockRouteLocators.LOCATOR_SVOY_MODE)

    @allure.step('Кликнуть на таб Быстрый')
    def click_fast_mode_tab(self):
        self.click_to_element(BlockRouteLocators.LOCATOR_FAST_MODE)

    @allure.step('Найти типы передвижения')
    def find_types(self):
        return self.find_elements(BlockRouteLocators.LOCATOR_TYPES_DISABLED)

    @allure.step('Кликнуть на кнопку Вызвать такси')
    def click_order_taxi_button(self):
        self.click_to_element(BlockRouteLocators.BUTTON_ORDER_TAXI)

    @allure.step('Проверка видимости кнопки Вызвать такси')
    def check_visibility_button_order_taxi(self):
        return self.find_element_with_wait(BlockRouteLocators.BUTTON_ORDER_TAXI).is_displayed()

    @allure.step('Проверка видимости кнопки Забронировать')
    def check_visibility_button_book_taxi(self):
        return self.find_element_with_wait(BlockRouteLocators.BUTTON_BOOK_TAXI).is_displayed()

    @allure.step('Кликнуть на тариф Свой режим Драйв')
    def click_svoy_mode_drive_type(self):
        self.click_to_element(BlockRouteLocators.SVOY_MODE_DRIVE_TYPE)