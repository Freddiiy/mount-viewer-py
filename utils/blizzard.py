import oauth
import requests
import urllib3

def get_data_from_api(region: str, path: str, params: dict):
    token = oauth.get_access_token()
    url = f"https://{region}.api.blizzard.com/{path}"
