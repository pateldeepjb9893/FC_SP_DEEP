from selenium.webdriver.common.by import By


class CookCountyLocator:
    ADVANCED_SEARCH_BUTTON = (By.XPATH, "(//*[text()='Advanced Search'])[1]")
    DOCUMENT_TYPE_SEARCH_ACCORDION = (By.XPATH, "//*[contains(text(),'Document Type Search')]")
    DOCUMENT_TYPE_DROPDOWN = (By.ID, "DocumentType")
    FROM_DATE = (By.XPATH, "//h2[@id='ItemThree']/following::input[@id='RecordedFromDate']")
    TO_DATE = (By.XPATH, "//h2[@id='ItemThree']/following::input[@id='RecordedToDate']")
    SEARCH_BUTTON = (By.XPATH, "(//h2[@id='ItemThree']/following::button[@type='submit'])[1]")
    VIEW_BUTTON = (By.XPATH, "(//a[text()='View'])")
    VIEW_DOCUMENT = (By.XPATH, "//a[contains(text(), 'View Document in New Window')]")
    BACK_BUTTON = (By.XPATH, "//a[text() = ' Back']")