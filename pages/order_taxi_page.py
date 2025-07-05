import allure
from locators.order_taxi_locators import OrderTaxiPageLocators
from pages.base_page import BasePage

class OrderTaxiPage(BasePage):

    @allure.step('Клик на кнопку Ввести номер и заказать')
    def click_enter_number_order_button(self):
        self.click_to_element(OrderTaxiPageLocators.BUTTON_ENTER_NUMBER_ORDER)

    @allure.step('Получение элементов со страницы ожидания такси')
    def check_waiting_page(self):
        title = self.get_text_from_element(OrderTaxiPageLocators.ORDER_HEADER_TITLE)
        time_counter = self.find_element_with_wait(OrderTaxiPageLocators.ORDER_HEADER_TIME).is_displayed()
        button_close = self.find_element_with_wait(OrderTaxiPageLocators.BUTTON_CLOSE).is_displayed()
        button_details = self.find_element_with_wait(OrderTaxiPageLocators.BUTTON_DETAILS).is_displayed()
        return title, time_counter, button_close, button_details

    @allure.step('Ожидание окончания таймера')
    def waiting_time(self):
       self.waiting_element(OrderTaxiPageLocators.CAR_NUMBER)

    @allure.step('Получение элементов с окна назначенного такси')
    def check_order_page_complete(self):
        title = self.get_text_from_element(OrderTaxiPageLocators.ORDER_HEADER_TITLE)
        car_number  = self.find_element_with_wait(OrderTaxiPageLocators.CAR_NUMBER).is_displayed()
        car_picture = self.find_element_with_wait(OrderTaxiPageLocators.CAR_PICTURE).is_displayed()
        driver_picture = self.find_element_with_wait(OrderTaxiPageLocators.DRIVER_PICTURE).is_displayed()
        rating = self.get_text_from_element(OrderTaxiPageLocators.RATING)
        driver_name = self.find_element_with_wait(OrderTaxiPageLocators.DRIVER_NAME).is_displayed()
        button_close = self.find_element_with_wait(OrderTaxiPageLocators.BUTTON_CLOSE).is_displayed()
        button_details = self.find_element_with_wait(OrderTaxiPageLocators.BUTTON_DETAILS).is_displayed()
        return title, car_number, car_picture, driver_picture, rating, driver_name, button_close, button_details

    @allure.step('Получение цены из Деталей')
    def get_price_order_page_complete_details(self):
        text = self.get_text_from_element(OrderTaxiPageLocators.DETAILS_PRICE)
        price = self.extract_numbers_with_regex(text)
        return price

    @allure.step('Клик на кнопку Детали')
    def click_details_order_complete(self):
        self.click_to_element(OrderTaxiPageLocators.BUTTON_DETAILS)

    @allure.step('Клик на кнопку Отменить')
    def click_close_order_complete(self):
        self.click_to_element(OrderTaxiPageLocators.BUTTON_CLOSE)