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


# first read the file data i.e usernames and password

def read_credentials(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username,password = row
        credentials.append({"username": username, "password": password})
        return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }

    response = post_request(url=auth_url(), auth=None, headers=common_headers(), json=payload)
    return response


def test_create_token_3times():
    file_path = "users.xlsx"
    credentials = read_credentials(file_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = make_request_auth(username, password)
        print(response)
