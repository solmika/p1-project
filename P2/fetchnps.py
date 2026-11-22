import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()
key = os.getenv("NPS_API_KEY")

user_input = input("Please enter a state code (e.g., WA, CA, NY): ")
url = "https://developer.nps.gov/api/v1/parks"
params = {"q": user_input, "api_key": key}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = (response.json())
    print("Search successful! Status Code:", response.status_code, "Reason:", response.reason)
    data_set = data["data"][0:5]
    #print(data_set)
    print([park['fullName'] for park in data["data"]])
else:
    print("I'm sorry, something's gone wrong. Status Code:", response.status_code, "Reason:", response.reason) 
