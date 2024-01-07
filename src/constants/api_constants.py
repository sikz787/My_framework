# add constants which stay same
import requests


def base_url():
    return "https://restful-booker.herokuapp.com"


def create_url():
    return "https://restful-booker.herokuapp.com/booking"


def auth_url():
    return "https://restful-booker.herokuapp.com/auth"


def put_url():
    return "https://restful-booker.herokuapp.com/"  # "/" + str(booking_id)
# you can also make above urls(only constant/foxed one) in class by creating class(self) and use @staticmethod before every method
