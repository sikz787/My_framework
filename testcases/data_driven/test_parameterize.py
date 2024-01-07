from src.helpers.api_requests_wrapper import post_request, put_request
from src.constants.api_constants import auth_url
from src.constants.api_constants import create_url
from src.helpers.utilities import common_headers, common_for_update
from src.helpers.payload_manager import payload_create
from src.helpers.payload_manager import payload_auth
from src.helpers.common_verficiations import verify_response, verify_status
from src.constants.api_constants import other_url

import openpyxl
import requests
import pytest
import json


# first read the file data i.e usernames and password

def read_credentials(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
        return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }

    response = post_request(url=auth_url(), auth=None, headers=common_headers(), json=payload)
    return response


@pytest.mark.parametrize("user_cred", read_credentials("datafile.xlsx"))
def test_create_token_3times(user_cred, make):
    username = user_cred["username"]
    password = user_cred["password"]
    response = make.request_auth(username, password)
    assert response.status_code == 200
