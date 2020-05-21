import requests

url = "http://127.0.0.1:8000/api/auth/"


def get_token():
    response = requests.post(url, data={'username': 'krishna', 'password': '0012'})
    return response.text

get_token()