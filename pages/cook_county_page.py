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
            self.scroll_to_element(element)
            element.click()
            time.sleep(3)
            details_map = {}
            all_names = []

            grantee_names_element = self.driver.find_elements(*CookCountyLocator.GRANTEES_NAME)
            names = [element.text.strip() for element in grantee_names_element if element.text.strip()]
            all_names.append(names)

            address = self.driver.find_element(*CookCountyLocator.ADDRESS_DETAILS).text.strip()
            documentNumber = self.driver.find_element(*CookCountyLocator.DOCUMENT_NUMBER).text.strip()

            details_map["Address"] = address
            details_map["DocumentNumber"] = documentNumber
            details_map["Names"] = all_names
            pin = self.get_text(CookCountyLocator.PROPERTY_INDEX_NUMBER)
            details_map["PropertyIndexNumber"] = pin
            self.create_or_update_excel(details_map)
            self.click(CookCountyLocator.BACK_BUTTON)
        self.sending_email()

    def extract_pdf_data(self):
        return self.extract_pdf_text_from_new_window()
