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

    @allure.step('Кликнуть на таб вида маршрута')
    def click_mode_tab(self, locator):
        self.click_to_element(locator)

    @allure.step('Найти типы передвижения')
    def find_types(self, locator):
        return self.find_elements(locator)

    @allure.step('Кликнуть на кнопку Вызвать такси')
    def click_order_taxi_button(self):
        self.click_to_element(BlockRouteLocators.BUTTON_ORDER_TAXI)