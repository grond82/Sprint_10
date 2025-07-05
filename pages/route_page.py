import allure
from locators.route_page_locators import RoutePageLocators
from url import TestUrl
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
        self.find_element_with_wait(RoutePageLocators.A_AND_B_LOCATORS)
        return self.find_elements(RoutePageLocators.A_AND_B_LOCATORS)

    def enter_route(self, first_address, second_address):
        self.go_to_url(TestUrl.HOMEPAGE_URL)
        self.enter_field_from(first_address)
        self.enter_field_to(second_address)
        self.find_a_b_route()