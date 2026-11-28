import requests
import json
import os

from dotenv import load_dotenv
def parks_by_state(typed_state):
    load_dotenv()
    key = os.getenv("NPS_API_KEY")
    url = "https://developer.nps.gov/api/v1/parks"
    params = {"stateCode": typed_state, "api_key": key}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Request failed. Your status code is", response.status_code, response.reason)
        return None

    return response.json()["data"]