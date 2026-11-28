import requests
import json
import os

from dotenv import load_dotenv
import pprint

load_dotenv()

def search_parks(term):
    try:
        key = os.getenv("NPS_API_KEY")
        FIELDS = "fullName,description"
        headers = {"NPS-User-Agent": "HCDE310 student project"}
        url = "https://developer.nps.gov/api/v1/parks"
        params ={"q": term, "fields": FIELDS, "api_key": key}
        r = requests.get(url,params=params,headers=headers,timeout=10)


    except requests.RequestException:
        return None


    if r.status_code != 200:
        return None


    data = (r.json())
   
    complete_results = (data["data"][:1])
    print(f"{len(data)} results found. Results:")
    print()
    return complete_results


results = search_parks("WA")
for c in results:
        print(f"Park name: {c['fullName']}\nDescription: {c['description']}\n")

    

