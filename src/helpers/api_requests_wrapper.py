# to make get,post,put,patch,delete. keep generic HTTP Methods, keep generic methods here and keep common functions.
import json

import requests


def get_request(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:  # means if response is in json return response
        return response.json()
    return response  # if not in json


def post_request(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response


def patch_request(url, auth, headers, payload, in_json):
    patch_response = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return patch_response


def put_request(url, auth, headers, payload, in_json):
    put_response = requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    return put_response


def delete_request(url, auth, headers, payload, in_json):
    delete_response = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return delete_response.json()
    return delete_response
