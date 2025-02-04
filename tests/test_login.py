import time

import pytest
from pages.cook_county_page import CookCountyPage
from pages.vane_county_page import VaneCountyPage
from config.config import COOK_COUNTY_URL
from config.config import VANE_COUNTY_URL
import requests


def test_searching_doc_cook_county(setup):
    driver = setup
    driver.get(COOK_COUNTY_URL)
    cook_county_page = CookCountyPage(driver)
    time.sleep(2)
    cook_county_page.search_doc()
    time.sleep(2)
    cook_county_page.view_doc()
    time.sleep(2)


def test_searching_doc_vane_county(setup):
    driver = setup
    driver.get(VANE_COUNTY_URL)
    vane_county_page = VaneCountyPage(driver)
    time.sleep(2)
    vane_county_page.search_doc()
    time.sleep(2)
    vane_county_page.view_doc()
    time.sleep(2)


# def test_sending_request_directly():
#     url = "https://lrscoreapi-kane-prod.azurewebsites.net/api/search/advanced"
#
#     # Headers
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer undefined"
#     }
#
#     # JSON payload
#     payload = {
#         "oGrantorGrantee": {
#             "Grantor": "",
#             "Grantee": "",
#             "GrantorOr": True,
#             "GrantorAnd": False,
#             "SearchType": 0
#         },
#         "oSubdivision": {
#             "SubdivisionId": 0,
#             "SubdivisionName": "",
#             "BlockId": 0,
#             "BlockName": "",
#             "LotId": 0,
#             "LotName": "",
#             "ParamSub": "",
#             "ParamBlock": "",
#             "ParamLot": ""
#         },
#         "oSection": {
#             "SectionId": 0,
#             "TownshipId": 0,
#             "RangeId": 0,
#             "QuadrantNE": False,
#             "QuadrantNW": False,
#             "QuadrantSE": False,
#             "QuadrantSW": False,
#             "QuadrantNENE": False,
#             "QuadrantNENW": False,
#             "QuadrantNESE": False,
#             "QuadrantNESW": False,
#             "QuadrantNWNE": False,
#             "QuadrantNWNW": False,
#             "QuadrantNWSE": False,
#             "QuadrantNWSW": False,
#             "QuadrantSENE": False,
#             "QuadrantSENW": False,
#             "QuadrantSESE": False,
#             "QuadrantSESW": False,
#             "QuadrantSWNE": False,
#             "QuadrantSWNW": False,
#             "QuadrantSWSE": False,
#             "QuadrantSWSW": False
#         },
#         "oPropertyAddress": {
#             "SearchType": 0
#         },
#         "oParcelNumber": {},
#         "oDocumentType": {
#             "InstrumentCodes": [
#                 "LP"
#             ]
#         },
#         "oDocumentNumber": {},
#         "oAssociatedDocumentNumber": {},
#         "oBNumber": {},
#         "oBNumberOriginal": {},
#         "oRemarks": {},
#         "oAdditional": {
#             "DateFiledFrom": "2025-01-27",
#             "DateFiledTo": "2025-01-27"
#         }
#     }
#
#     # Make the request
#     response = requests.post(url, headers=headers, json=payload)
#     api_response = response.json()
#     # Print the response
#     print("Status Code:", api_response)
