from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import re


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_to_element(self,locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def enter_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def go_to_url(self, url):
        self.driver.get(url)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def move_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def maximize_window(self):
        self.driver.maximize_window()

    def extract_numbers_with_regex(self, text):
        return re.findall(r'\d+', text)

    def waiting_element(self, locator):
        WebDriverWait(self.driver, 55).until(expected_conditions.visibility_of_element_located(locator))