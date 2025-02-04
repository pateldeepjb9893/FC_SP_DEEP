import os
import time
from locators.vane_county_locators import VaneCountyLocator
from pages.base_page import BasePage


class VaneCountyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_doc(self):
        self.scroll_to_element(VaneCountyLocator.DOCUMENT_TYPE_DROPDOWN)
        time.sleep(5)
        self.select_dropdown_option("instrumentCode", "45: 'LP'", select_type="value")
        self.send_date(VaneCountyLocator.FROM_DATE)
        self.send_date(VaneCountyLocator.TO_DATE)
        self.click(VaneCountyLocator.SEARCH_BUTTON)

    def view_doc(self):
        view_pdf_elements = self.driver.find_elements(*VaneCountyLocator.VIEW_PDF)

        for element in view_pdf_elements:
            element.click()
            time.sleep(7)
            self.switch_to_frame(VaneCountyLocator.FRAME_LOCATOR)
            self.click(VaneCountyLocator.PRINT_OPTION)
            try:
                self.extract_pdf_text_from_new_window()
            except Exception as e:
                print(f"Error processing page")
                continue
            self.driver.switch_to.default_content()
            self.click(VaneCountyLocator.CLOSE_BUTTON)

        self.process_ocr_files_and_save_to_excel()
        directory = "propertyDetails"
        try:
            files = [f for f in os.listdir(directory) if f.endswith(".xlsx")]

            if not files:
                print("No Excel files found in the directory.")
                return

            print(f"Found {len(files)} Excel file(s) in {directory}: {files}")

            for file in files:
                file_path = os.path.join(directory, file)
                print(f"Processing file: {file_path}")

                self.extract_and_store_names(file_path)

            print("Completed processing all files.")

        except Exception as e:
            print(f"Error processing files in directory: {e}")

    def extract_pdf_data(self):
        return self.extract_pdf_text_from_new_window()
