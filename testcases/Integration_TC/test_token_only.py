from src.constants.api_constants import auth_url
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verficiations import verify_response, verify_status
from src.helpers.payload_manager import payload_auth
from src.helpers.utilities import common_headers


def test_only_token():
    response = post_request(url=auth_url(), auth=None, headers=common_headers(), payload=payload_auth(),
                            in_json=False)
    verify_status(response, 200)
    token1 = response.json()["token"]
    print(token1)
    verify_response(token1)
    return token1
