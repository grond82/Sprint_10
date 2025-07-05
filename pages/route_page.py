import allure
from locators.route_page_locators import RoutePageLocators
from pages.base_page import BasePage

class RoutePage(BasePage):

    @allure.step('Заполнить поле Откуда')
    def enter_field_from(self, address):
        self.enter_text_to_element(RoutePageLocators.FIELD_FROM, address)

    @allure.step('Заполнить поле Куда')
    def enter_field_to(self, address):
        self.enter_text_to_element(RoutePageLocators.FIELD_TO, address)

    @allure.step('Найти начальную и конечную точку маршрута')
    def find_a_b_route(self):
        return self.find_elements(RoutePageLocators.A_AND_B_LOCATORS)