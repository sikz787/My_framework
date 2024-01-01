# keep common headers in it, means things which are common everytime like files, headers.We can also keep common functions to read data from files like csv, excel.


def common_headers():
    headers = {
        "Content-Type": "application/json",
    }
    return headers


def common_for_update():
    headers = {
        "Content-type" : "application/json",
        "Authorization" : "Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
