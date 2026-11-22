import requests
import json
import pprint

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 52.52,
	"longitude": -122.33,
	"daily": ["temperature_2m_max", "temperature_2m_min", "uv_index_max", "wind_speed_10m_max", "precipitation_probability_max"],
	"timezone": "auto",
    "wind_speed_unit": "mph",
	"temperature_unit": "fahrenheit",
	"precipitation_unit": "inch",
	"start_date": "2026-11-21",
	"end_date": "2026-11-22",
}
response = requests.get(url,params=params, timeout=10)

# Function to display weather data from the API response
def display_weather_data(data):
    for i in range(len(data['daily']['time'])):
        print(f"Date: {data['daily']['time'][i]}")
        print(f"Max Temperature: {data['daily']['temperature_2m_max'][i]} degrees Fahrenheit")
        print(f"Min Temperature: {data['daily']['temperature_2m_min'][i]} degrees Fahrenheit")
        print(f"UV Index: {data['daily']['uv_index_max'][i]}")
        print(f"Max Wind Speed: {data['daily']['wind_speed_10m_max'][i]} mph")
        print(f"Precipitation Probability: {data['daily']['precipitation_probability_max'][i]}%")
        print()

if response.status_code == 200:
    data = (response.json())
    display_weather_data(data)
    #pprint.pprint(data)
else:
    print("Status Code:", response.status_code, "Reason:", response.reason) 

print("https://open-meteo.com/")
print("Weather data by Open-Meteo.com")
