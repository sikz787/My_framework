from src.helpers.api_requests_wrapper import post_request, put_request
from src.constants.api_constants import auth_url
from src.constants.api_constants import create_url
from src.helpers.utilities import common_headers, common_for_update
from src.helpers.payload_manager import payload_create
from src.helpers.payload_manager import payload_auth
from src.helpers.common_verficiations import verify_response, verify_status
from src.constants.api_constants import put_url

# removed - both token and create booking functions from this file and it will pick this from conftest file
import pytest


class Testall(object):

    def test_update_booking1(self, create_booking1, token):
        booking_id = create_booking1
        url = create_url() + "/" + str(booking_id)
        response = put_request(url=url, auth=None, headers=common_for_update(), payload=payload_create(),
                               in_json=False)
        print(response)
        return response

    def test_delete_booking1(self, create_booking1, token):
        booking_id = create_booking1
        delete_url = create_url() + "/" + booking_id
        response = put_request(url=delete_url, auth=None, headers=common_for_update(), payload=None, in_json=False)
        print(response.json())
        return response
