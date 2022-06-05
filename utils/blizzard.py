import oauth
import requests


def get_data_from_api(region: str, path: str, params: dict):
    params["access_token"] = oauth.get_access_token()
    url = f"https://{region}.api.blizzard.com{path}"

    response = requests.get(url, params)
    return response.json()
