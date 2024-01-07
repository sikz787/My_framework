from dotenv import load_dotenv
import os


def test_auth():
    load_dotenv()
    username = os.getenv("username")
    password = os.getenv("password")
    print(username,password)

