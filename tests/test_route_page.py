import allure
from url import TestUrl
from pages.route_page import RoutePage
from locators.route_page_locators import RoutePageLocators
from data import Data

class TestRoutePage:

    @allure.title('Проверка отрисовки маршрута')
    def test_fill_in_route(self,driver):
        route_page = RoutePage(driver)
        route_page.go_to_url(TestUrl.HOMEPAGE_URL)
        route_page.enter_field_from(Data.FIRST_ADDRESS)
        route_page.enter_field_to(Data.SECOND_ADDRESS)
        route_page.find_element_with_wait(RoutePageLocators.A_AND_B_LOCATORS)
        a_b = route_page.find_a_b_route()
        assert a_b[0].text == "улица Хамовнический Вал, 34" and a_b[1].text == "Зубовский бульвар, 37"