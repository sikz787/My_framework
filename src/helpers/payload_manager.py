# to create something we need data which we can keep here

def payload_auth():

    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload

def payload_create():
    payload = {
        "firstname": "sik",
        "lastname": "tyagi",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "super bowls"
    }
    return payload
