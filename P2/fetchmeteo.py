import requests
import json
import pprint

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"daily": ["temperature_2m_max", "temperature_2m_min", "uv_index_max", "wind_speed_10m_max", "precipitation_sum", "precipitation_probability_max"],
	"timezone": "auto",
	"forecast_days": 2,
}
response = requests.get(url,params=params, timeout=10)

if response.status_code == 200:
    data = (response.json())
    pprint.pprint(data)
else:
    print("Status Code:", response.status_code, "Reason:", response.reason) 

print("https://open-meteo.com/")
print("Weather data by Open-Meteo.com")
