import requests
import json
import pprint

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 52.52,
	"longitude": -122.33,
    "temperature_unit": "fahrenheit",
	"hourly": "temperature_2m",
    "forecast_hours": 4
}
response = requests.get(url,params=params)

if response.status_code == 200:
    data = (response.json())
    pprint.pprint(data)
else:
    print("Status Code:", response.status_code, "Reason:", response.reason) 
