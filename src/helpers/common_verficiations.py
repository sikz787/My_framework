# to verify HTTP Status codes and common verifications, like content type, headers, json schema and data


def verify_status(response_data, expected_data):
    assert response_data.status_code == expected_data, "Status code" + "/" + str(expected_data)


def verify_body_not_null(key):
    assert key != 0, "key is not blank" + key
    assert key > 0, "key is greater then zero"


def verify_response(key):
    assert key is not None


def verify_response_time():
    pass
