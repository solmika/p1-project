import requests
import json
import os

from dotenv import load_dotenv
import pprint

load_dotenv()


def search_parks(term):
    try:
        key = os.getenv("NPS_API_KEY")
        FIELDS = "line2,description,thumbnail"
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

# camp_url = "https://developer.nps.gov/api/v1/campgrounds"
# camp_res = requests.get(camp_url, params=params).json()
# for camp in camp_res["data"]:
#     print("Name:", camp.get("name", "N/A"))
#     print("Description:", camp.get("description", "N/A"))



# to_do_url = "https://developer.nps.gov/api/v1/thingstodo"
# to_do_res = requests.get(to_do_url, params=params).json()
# for to_do in to_do_res["data"]:
#     print()
#     print("Name:", to_do.get("title", "N/A"))
#     print()
#     print("Location:", to_do.get("locationDescription", "N/A"))
#     print()
#     print("Duration:", to_do.get("shortDescription", "N/A"))
    

