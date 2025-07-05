from selenium.webdriver.common.by import By

class BlockRouteLocators:
    BLOCK_ROUTE = By.XPATH, "//div[contains(@class, 'type-picker shown')]"
    LOCATOR_PRICE = By.CLASS_NAME, "text"
    LOCATOR_DURATION = By.CLASS_NAME, "duration"
    LOCATOR_ACTIVE_MODE = By.XPATH, "//div[contains(@class, 'mode active')]"
    LOCATOR_OPTIMAL_MODE = By.XPATH, "//div[contains(text(), 'Оптимальный')]"
    LOCATOR_FAST_MODE = By.XPATH, "//div[contains(text(), 'Быстрый')]"
    LOCATOR_SVOY_MODE = By.XPATH, "//div[contains(text(), 'Свой')]"
    LOCATOR_TYPES_CONTAINER = By.XPATH, "//div[contains(@class, 'types-container')]"
    LOCATOR_TYPES_ACTIVE = By.XPATH, "//div[contains(@class, 'types-container')]/div[contains(@class, 'type')]"
    LOCATOR_TYPES_DISABLED = By.XPATH, "//div[contains(@class, 'types-container')]/div[contains(@class, 'type') and contains(@class, 'disabled')]"
    BUTTON_ORDER_TAXI = By.XPATH, "//button[contains(text(), 'Вызвать такси')]"
    SVOY_MODE_DRIVE_TYPE = By.XPATH, "//div[contains(@class, 'type drive')]"
    BUTTON_BOOK_TAXI = By.XPATH, "//button[contains(text(), 'Забронировать')]"