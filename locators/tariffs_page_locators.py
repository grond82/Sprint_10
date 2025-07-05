from selenium.webdriver.common.by import By

class TariffsPageLocators:
    TARIFFS_LOCATOR = By.CLASS_NAME, "tcard-title"
    TARIFF_WORK_ACTIVE = By.XPATH, "//div[contains(text(), 'Рабочий')]/.."
    PHONE_LOCATOR = By.CLASS_NAME, "np-text"
    PAYMENT_METHOD_LOCATOR = By.CLASS_NAME, "pp-text"
    COMMENT_LOCATOR = By.ID, "comment"
    REQUIREMENTS_LOCATOR = By.CLASS_NAME, "reqs-head"
    TARIFF_INFO_ACTIVE = By.XPATH, "//div[contains(@class, 'tcard active')]/button"
    LOCATOR_FOR_TESTING_ACTIVE_TARIFF = By.XPATH, "//div[contains(@class, 'tcard active')]/div[contains(@class, 'tcard-title')]"
    LOCATOR_FOR_TESTING_HOVER_TARIFF_INFO = By.XPATH, "//div[contains(@class, 'show border')]/div[@class='i-floating']/div[@class='i-title']"
    LOCATOR_FOR_TESTING_HOVER_TARIFF_DESCRIPTION = By.XPATH, "//div[contains(@class, 'show border')]/div[@class='i-floating']/div[@class='i-dPrefix']"
    CHECKBOX_TABLE_FOR_NOTEBOOK = By.XPATH, "//span[contains(@class, 'slider round')]"
    PRICE_WORK_TARIFF = By.XPATH, "//div[contains(text(), 'Рабочий')]/following-sibling::div"