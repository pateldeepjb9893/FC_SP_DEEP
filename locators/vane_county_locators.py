from selenium.webdriver.common.by import By


class VaneCountyLocator:
    DOCUMENT_TYPE_DROPDOWN = (By.ID, "instrumentCode")
    FROM_DATE = (By.XPATH, "//*[@id='dateFiledFrom']")
    TO_DATE = (By.XPATH, "//*[@id='dateFiledTo']")
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Search']")
    VIEW_PDF = (By.XPATH, "(//i[@class='fa fa-paperclip'])")
    FRAME_LOCATOR = (By.ID, "image_iframe")
    PRINT_OPTION = (By.XPATH, "//*[@title= 'Save Image']")
    CLOSE_BUTTON = (By.XPATH, "//button[text()='Close']")
    NAME_LOCATOR = (By.XPATH, "(//*[@class='recordsScroll'])[2]/a")
