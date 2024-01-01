from src.helpers.api_requests_wrapper import post_request, put_request
from src.constants.api_constants import auth_url
from src.constants.api_constants import create_url
from src.helpers.utilities import common_headers
from src.helpers.payload_manager import payload_create
from src.helpers.payload_manager import payload_auth
from src.helpers.common_verficiations import verify_response, verify_status
from src.constants.api_constants import other_url

import requests

import token

import pytest


class Testall2(object):

    @pytest.mark.positive
    def test_create_booking1(self):
        response = post_request(url=create_url(), auth=None, headers=common_headers(), payload=payload_create(),
                                in_json=False)
        print(response)
        verify_response(response.json()["bookingid"])
        verify_status(response, 200)
        booking_id = (response.json()["bookingid"])
        print(booking_id)
        return booking_id

    def test_update_booking1(self):
        # .token = "62564a1e08415f"
        url = "create_url" + "/" + "booking_id"
        booking_id = self.test_create_booking1()
        auth = payload_auth()
        headers = common_headers()
        payload = payload_create()
        response = put_request(url=url, auth=None, headers=common_headers(), payload=payload_create(),
                               in_json=False)
        print(response)
        verify_response(response.json()["bookingid"])
        verify_status(response, 200)
        booking_id = (response.json()["bookingid"])
        print(booking_id)
        return booking_id
