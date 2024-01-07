from src.helpers.api_requests_wrapper import post_request, put_request
from src.constants.api_constants import auth_url
from src.constants.api_constants import create_url
from src.helpers.utilities import common_headers, common_for_update
from src.helpers.payload_manager import payload_create
from src.helpers.payload_manager import payload_auth
from src.helpers.common_verficiations import verify_response, verify_status
from src.constants.api_constants import put_url

import pytest


class Testall(object):

    @pytest.fixture()
    def token(self):
        response = post_request(url=auth_url(), auth=None, headers=common_headers(), payload=payload_auth(),
                                in_json=False)
        verify_status(response, 200)
        token_crud = response.json()["token"]
        print(token_crud)
        verify_response(token_crud)
        return token_crud

    @pytest.fixture()
    def create_booking1(self):
        response = post_request(url=create_url(), auth=None, headers=common_headers(), payload=payload_create(),
                                in_json=False)
        print(response)
        verify_response(response.json()["bookingid"])
        verify_status(response, 200)
        booking_id = (response.json()["bookingid"])
        print(booking_id)
        return booking_id

    def test_update_booking1(self, create_booking1, token):
        booking_id = create_booking1
        url = create_url() + "/ "+str(booking_id)
        auth = ("admin", "password123")
        response = put_request(url=url, auth=None, headers=common_for_update(), payload=payload_create(),
                               in_json=False)
        print(response)
