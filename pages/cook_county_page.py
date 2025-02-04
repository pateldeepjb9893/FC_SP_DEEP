import os, pdfplumber
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
from locators.cook_county_locators import CookCountyLocator
from pages.base_page import BasePage
import time


class CookCountyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_doc(self):
        self.click(CookCountyLocator.ADVANCED_SEARCH_BUTTON)
        self.click(CookCountyLocator.DOCUMENT_TYPE_SEARCH_ACCORDION)
        self.click(CookCountyLocator.DOCUMENT_TYPE_DROPDOWN)
        self.select_dropdown_option("DocumentType", "LISF", select_type="value")
        self.send_date(CookCountyLocator.FROM_DATE)
        self.send_date(CookCountyLocator.TO_DATE)
        self.click(CookCountyLocator.SEARCH_BUTTON)

    def view_doc(self):
        view_pdf_elements = self.driver.find_elements(*CookCountyLocator.VIEW_BUTTON)

        for element in view_pdf_elements:
            element.click()
            time.sleep(7)
            self.click(CookCountyLocator.VIEW_DOCUMENT)
            try:
                self.extract_pdf_text_from_new_window()
            except Exception as e:
                print(f"Error processing page")
                continue
            self.driver.switch_to.default_content()
            self.click(CookCountyLocator.BACK_BUTTON)

    def extract_pdf_data(self):
        return self.extract_pdf_text_from_new_window()
