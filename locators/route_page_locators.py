from selenium.webdriver.common.by import By

class RoutePageLocators:
    FIELD_FROM = By.ID, "from"
    FIELD_TO = By.ID, "to"
    A_AND_B_LOCATORS = By.XPATH, "//ymaps[contains(@id, 'id_')]/ymaps"