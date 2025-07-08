import allure
from locators.tariffs_page_locators import TariffsPageLocators
from pages.base_page import BasePage

class TariffPage(BasePage):

    @allure.step('Найти все тарифы')
    def find_all_tariffs(self):
        self.find_element_with_wait(TariffsPageLocators.TARIFF_WORK_ACTIVE)
        return self.find_elements(TariffsPageLocators.TARIFFS_LOCATOR)

    @allure.step('Получить названия тарифов')
    def get_tariffs_name_on_page(self):
        tariffs_on_page = self.find_all_tariffs()
        tariffs_name_on_page = []
        for tariff in tariffs_on_page:
            tariffs_name_on_page.append(tariff.text)
        return tariffs_name_on_page

    @allure.step('Проверка отображения всех тарифных опций')
    def check_block_tariff_options(self):
        all_elements_tariff_options = self.all_elements_tariff_options()
        all_displayed = all(element.is_displayed() for element in all_elements_tariff_options)
        return all_displayed

    @allure.step('Получение всех тарифных опций')
    def all_elements_tariff_options(self):
        all_elements_tariff_options = [self.find_element_with_wait(TariffsPageLocators.PHONE_LOCATOR),
                                       self.find_element_with_wait(TariffsPageLocators.PAYMENT_METHOD_LOCATOR),
                                       self.find_element_with_wait(TariffsPageLocators.COMMENT_LOCATOR),
                                       self.find_element_with_wait(TariffsPageLocators.REQUIREMENTS_LOCATOR)]
        return all_elements_tariff_options

    @allure.step('Переключение тарифов')
    def click_tariffs(self,tariff_name):
        tariffs = self.find_elements(TariffsPageLocators.TARIFFS_LOCATOR)
        for tariff in tariffs:
            if tariff.text == tariff_name:
                tariff.click()

    @allure.step('Наведение на иконку информации тарифа')
    def hover_mouse_tariff_info(self):
        self.move_to_element(TariffsPageLocators.TARIFF_INFO_ACTIVE)

    @allure.step('Получение названия активного тарифа и информации о тарифе')
    def get_name_tariff_active_and_info(self):
        tariff_name = self.get_text_from_element(TariffsPageLocators.LOCATOR_FOR_TESTING_ACTIVE_TARIFF)
        tariff_name_info = self.get_text_from_element(TariffsPageLocators.LOCATOR_FOR_TESTING_HOVER_TARIFF_INFO)
        tariff_description = self.get_text_from_element(TariffsPageLocators.LOCATOR_FOR_TESTING_HOVER_TARIFF_DESCRIPTION)
        return tariff_name, tariff_name_info, tariff_description

    @allure.step('Кликнуть на чекбокс Столик для ноутбука')
    def click_checkbox_table_for_notebook(self):
        self.click_to_element(TariffsPageLocators.CHECKBOX_TABLE_FOR_NOTEBOOK)

    @allure.step('Получения цены тарифа')
    def get_price_work_tariff(self):
        text = self.get_text_from_element(TariffsPageLocators.PRICE_WORK_TARIFF)
        price = self.extract_numbers_with_regex(text)
        return price

    @allure.step('Получения активного тарифа')
    def get_active_tariff(self):
        return self.find_element_with_wait(TariffsPageLocators.TARIFF_WORK_ACTIVE)

    @allure.step('Клик на Требования к заказу')
    def click_requirements(self):
        self.click_to_element(TariffsPageLocators.REQUIREMENTS_LOCATOR)