# testing create booking
import json

from faker.providers import file

from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import create_url
from src.helpers.utilities import common_headers
from src.helpers.payload_manager import payload_create
from src.helpers.common_verficiations import verify_response, verify_status

import requests
import json
# import functions as well from destination, see above
# instead of creating different TC we will write them in class
# @pytest.mark.positive to mark your TCs
import pytest

from jsonschema import validate
from jsonschema.exceptions import ValidationError


class TestCreateBooking(object):

    # if you do not want to keep schema data like below, you can create new function, load schema, r stands for read
    @pytest.mark.positive
    def test_create_booking1(self):
        response = post_request(url=create_url(), auth=None, headers=common_headers(), payload=payload_create(),
                                in_json=False)
        print(response)
        verify_response(response.json()["bookingid"])
        verify_status(response, 200)
        booking_id = (response.json()["bookingid"])
        print(booking_id)
        response_json = response.json()

    with open("C:\Users\User\PycharmProjects\My_framework\testcases\json_schema\schema"):
        schema = json.load(file)
        #         {
        #     "$schema": "https://json-schema.org/draft/2019-09/schema",
        #     "$id": "http://example.com/example.json",
        #     "type": "object",
        #     "default": {},
        #     "title": "Root Schema",
        #     "required": [
        #         "bookingid",
        #         "booking"
        #     ],
        #     "properties": {
        #         "bookingid": {
        #             "type": "integer",
        #             "default": 0,
        #             "title": "The bookingid Schema",
        #             "examples": [
        #                 4830
        #             ]
        #         },
        #         "booking": {
        #             "type": "object",
        #             "default": {},
        #             "title": "The booking Schema",
        #             "required": [
        #                 "firstname",
        #                 "lastname",
        #                 "totalprice",
        #                 "depositpaid",
        #                 "bookingdates",
        #                 "additionalneeds"
        #             ],
        #             "properties": {
        #                 "firstname": {
        #                     "type": "string",
        #                     "default": "",
        #                     "title": "The firstname Schema",
        #                     "examples": [
        #                         "sikander"
        #                     ]
        #                 },
        #                 "lastname": {
        #                     "type": "string",
        #                     "default": "",
        #                     "title": "The lastname Schema",
        #                     "examples": [
        #                         "Tyagi"
        #                     ]
        #                 },
        #                 "totalprice": {
        #                     "type": "integer",
        #                     "default": 0,
        #                     "title": "The totalprice Schema",
        #                     "examples": [
        #                         999
        #                     ]
        #                 },
        #                 "depositpaid": {
        #                     "type": "boolean",
        #                     "default": False,
        #                     "title": "The depositpaid Schema",
        #                     "examples": [
        #                         True
        #                     ]
        #                 },
        #                 "bookingdates": {
        #                     "type": "object",
        #                     "default": {},
        #                     "title": "The bookingdates Schema",
        #                     "required": [
        #                         "checkin",
        #                         "checkout"
        #                     ],
        #                     "properties": {
        #                         "checkin": {
        #                             "type": "string",
        #                             "default": "",
        #                             "title": "The checkin Schema",
        #                             "examples": [
        #                                 "2018-01-01"
        #                             ]
        #                         },
        #                         "checkout": {
        #                             "type": "string",
        #                             "default": "",
        #                             "title": "The checkout Schema",
        #                             "examples": [
        #                                 "2019-01-01"
        #                             ]
        #                         }
        #                     },
        #                     "examples": [{
        #                         "checkin": "2018-01-01",
        #                         "checkout": "2019-01-01"
        #                     }]
        #                 },
        #                 "additionalneeds": {
        #                     "type": "string",
        #                     "default": "",
        #                     "title": "The additionalneeds Schema",
        #                     "examples": [
        #                         "Breakfast"
        #                     ]
        #                 }
        #             },
        #             "examples": [{
        #                 "firstname": "sikander",
        #                 "lastname": "Tyagi",
        #                 "totalprice": 999,
        #                 "depositpaid": True,
        #                 "bookingdates": {
        #                     "checkin": "2018-01-01",
        #                     "checkout": "2019-01-01"
        #                 },
        #                 "additionalneeds": "Breakfast"
        #             }]
        #         }
        #     },
        #     "examples": [{
        #         "bookingid": 4830,
        #         "booking": {
        #             "firstname": "sikander",
        #             "lastname": "Tyagi",
        #             "totalprice": 999,
        #             "depositpaid": True,
        #             "bookingdates": {
        #                 "checkin": "2018-01-01",
        #                 "checkout": "2019-01-01"
        #             },
        #             "additionalneeds": "Breakfast"
        #         }
        #     }]
        # }
        try:
            validate(instance=response_json, schema=schema)
        except ValidationError as e:
            print(e.message)
