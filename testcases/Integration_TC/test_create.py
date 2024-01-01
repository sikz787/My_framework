from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import create_url
from src.helpers.utilities import common_headers
from src.helpers.payload_manager import payload_create
from src.helpers.common_verficiations import verify_response, verify_status

import requests
import pytest

# import functions as well from destination, see above
# instead of creating different TC we will write them in class
# @pytest.mark.positive to mark your TCs
import pytest


class TestCreateBooking(object):
    @pytest.mark.positive
    def test_create_booking1(self):
        response = post_request(url=create_url(), auth=None, headers=common_headers(), payload=payload_create(),
                                in_json=False)
        print(response)
        verify_response(response.json()["bookingid"])
        verify_status(response, 200)
        booking_id = (response.json()["bookingid"])
        print(booking_id)

    @pytest.mark.positive
    # no payload, try with None 400, if blank then 500
    def test_create_booking2(self):
        response = post_request(url=create_url(), auth=None, headers=common_headers(), payload=None, in_json=False)
        print(response)
        # verify_response(response.json()["bookingid"])
        verify_status(response, 400)
        # booking_id = (response.json()["bookingid"])
        # print(booking_id)

    @pytest.mark.positive
    # no payload, try with None 400, if blank {} then 500
    def test_create_booking3(self):
        response = post_request(url=create_url(), auth=None, headers=common_headers(), payload={}, in_json=False)
        print(response)
        # verify_response(response.json()["bookingid"])
        verify_status(response, 500)
        # booking_id = (response.json()["bookingid"])
        # print(booking_id)
