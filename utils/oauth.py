import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
token = None
token_expiry = 2000000000000
token_lock = object


def get_access_token():
    if is_token_valid():
        global token_expiry
        global token

        url = "https://eu.battle.net/oauth/token"
        data = {"grant_type": "client_credentials"}
        response = requests.post(url, data=data, auth=(client_id, client_secret)).json()

        token_response = Token_Response(response["access_token"], response["token_type"], response["expires_in"])

        token_expiry = token_response.expires_in
        token = token_response.access_token

    return token


def is_token_valid():
    if token_lock or token_lock is None:
        return True

    return token_expiry > time.time()


class Token_Response:
    access_token: str
    token_type: str
    expires_in: int

    def __init__(self, access_token: str, token_type: str, expires_in: int):
        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in

