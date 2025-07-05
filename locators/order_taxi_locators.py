from selenium.webdriver.common.by import By

class OrderTaxiPageLocators:
    BUTTON_ENTER_NUMBER_ORDER = By.CLASS_NAME, "smart-button"
    ORDER_HEADER_TITLE = By.CLASS_NAME, "order-header-title"
    ORDER_HEADER_TIME = By.CLASS_NAME, "order-header-time"
    BUTTON_CLOSE = By.XPATH, "//div[contains(text(), 'Отменить')]/preceding-sibling::button"
    BUTTON_DETAILS = By.XPATH, "//div[contains(text(), 'Детали')]/preceding-sibling::button"
    CAR_NUMBER = By.CLASS_NAME, "number"
    CAR_PICTURE = By.XPATH, "//img[contains(@alt, 'Car')]"
    DRIVER_PICTURE = By.XPATH, "//img[contains(@src, 'bender')]"
    RATING = By.CLASS_NAME, "order-btn-rating"
    DRIVER_NAME = By.XPATH, "//div[contains(@style, 'cursor')]"
    DETAILS_PRICE = By.XPATH, "//div[contains(text(), 'Стоимость - ')]"

