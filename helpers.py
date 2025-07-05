from url import TestUrl
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.route_page_locators import RoutePageLocators

class Helpers:

    def route(self,driver):
        driver.get(TestUrl.HOMEPAGE_URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(RoutePageLocators.FIELD_FROM))
        driver.find_element(*RoutePageLocators.FIELD_FROM).send_keys(Data.FIRST_ADDRESS)
        driver.find_element(*RoutePageLocators.FIELD_TO).send_keys(Data.SECOND_ADDRESS)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(RoutePageLocators.A_AND_B_LOCATORS))