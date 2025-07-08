import allure
from pages.route_page import RoutePage
from data import Data

class TestRoutePage:

    @allure.title('Проверка отрисовки маршрута')
    def test_fill_in_route(self,driver):
        route_page = RoutePage(driver)
        route_page.enter_route(Data.FIRST_ADDRESS, Data.SECOND_ADDRESS)
        route_page.enter_field_from(Data.FIRST_ADDRESS)
        route_page.enter_field_to(Data.SECOND_ADDRESS)
        a_b = route_page.find_a_b_route()
        assert a_b[0].text == Data.CHECK_FIRST_ADDRESS and a_b[1].text == Data.SECOND_ADDRESS