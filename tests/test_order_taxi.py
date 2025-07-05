import allure
import pytest
from pages.block_route_page import BlockRoute
from locators.order_taxi_locators import OrderTaxiPageLocators
from pages.order_taxi_page import OrderTaxiPage
from pages.tariffs_page import TariffPage
from locators.tariffs_page_locators import TariffsPageLocators
from helpers import Helpers


class TestOrderTaxi:

    @allure.title('Проверка окна ожидания такси и его элементов')
    def test_order_taxi_waiting_page(self, driver):
        route = Helpers()
        route.route(driver)
        block_route = BlockRoute(driver)
        block_route.click_order_taxi_button()
        tariff_page = TariffPage(driver)
        tariff_page.click_to_element(TariffsPageLocators.REQUIREMENTS_LOCATOR)
        tariff_page.click_checkbox_table_for_notebook()
        tariff_page.click_checkbox_table_for_notebook()
        order_taxi_page = OrderTaxiPage(driver)
        order_taxi_page.click_enter_number_order_button()
        title, time_counter, button_close, button_details = order_taxi_page.check_waiting_page()
        assert title == "Поиск машины" and time_counter == True and button_close == True and button_details == True

    @allure.title('Проверка окна совершенного заказа и его элементов')
    def test_order_taxi_complete_page(self, driver):
        route = Helpers()
        route.route(driver)
        block_route = BlockRoute(driver)
        block_route.click_order_taxi_button()
        order_taxi_page = OrderTaxiPage(driver)
        order_taxi_page.click_enter_number_order_button()
        order_taxi_page.waiting_time()
        title, car_number, car_picture, driver_picture, rating, driver_name, button_close, button_details = order_taxi_page.check_order_page_complete()
        assert "мин. и приедет" in title and car_number == True and car_picture == True and driver_picture == True and rating == '4,9' and driver_name == True and button_close == True and button_details == True

    @allure.title('Проверка что стоимость одинакова')
    def test_price_work_tariff_tariff_page_and_order_taxi_page(self, driver):
        route = Helpers()
        route.route(driver)
        block_route = BlockRoute(driver)
        block_route.click_order_taxi_button()
        order_taxi_page = OrderTaxiPage(driver)
        tariff_page = TariffPage(driver)
        tariff_price = tariff_page.get_price_work_tariff()
        order_taxi_page.click_enter_number_order_button()
        order_taxi_page.waiting_time()
        order_taxi_page.click_details_order_complete()
        tariff_price_order_complete = order_taxi_page.get_price_order_page_complete_details()
        assert tariff_price == tariff_price_order_complete

    @allure.title('Проверка работы кнопки Отмена')
    @pytest.mark.xfail(reason="Баг с неработающей кнопкой Отменить в окошке Заказа такси")
    def test_close_order_complete(self, driver):
        route = Helpers()
        route.route(driver)
        block_route = BlockRoute(driver)
        block_route.click_order_taxi_button()
        order_taxi_page = OrderTaxiPage(driver)
        order_taxi_page.click_enter_number_order_button()
        order_taxi_page.waiting_time()
        order_taxi_page.click_close_order_complete()
        assert order_taxi_page.find_element_with_wait(OrderTaxiPageLocators.BUTTON_CLOSE).is_displayed() != True