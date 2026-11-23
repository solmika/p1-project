import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()
key = os.getenv("NPS_API_KEY")
url = "https://developer.nps.gov/api/v1/parks"
params = {"parkCode": "olym", "api_key": key}
response = requests.get(url, params=params)

camp_url = "https://developer.nps.gov/api/v1/campgrounds"
camp_res = requests.get(camp_url, params=params).json()
for camp in camp_res["data"]:
    print("Name:", camp.get("name", "N/A"))
    print("Description:", camp.get("description", "N/A"))
    print("Booking Link:", camp.get("reservationUrl", "N/A"))


to_do_url = "https://developer.nps.gov/api/v1/thingstodo"
to_do_res = requests.get(to_do_url, params=params).json()
for to_do in to_do_res["data"]:
    print()
    print("Name:", to_do.get("title", "N/A"))
    print()
    print("Location:", to_do.get("locationDescription", "N/A"))
    print()
    print("Duration:", to_do.get("shortDescription", "N/A"))
    

