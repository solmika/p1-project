import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()
key = os.getenv("NPS_API_KEY")

# url = "https://developer.nps.gov/api/v1/amenities"
# params = {"parkCode": ["acad","dena"], "api_key": key}
# response = requests.get(url,params=params)
url = "https://developer.nps.gov/api/v1/parks?parkCode=&stateCode=&limit=10&start=0&q=stateCode&api_key=" + key
response = requests.get(url)

if response.status_code == 200:
    data = (response.json())
    print("Search successful! Status Code:", response.status_code, "Reason:", response.reason)
    data_set = data["data"][0:5]
    #print(data_set)
    print([park['fullName'] for park in data["data"]])
else:
    print("I'm sorry, something's gone wrong. Status Code:", response.status_code, "Reason:", response.reason) 
