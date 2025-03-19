import requests
from twilio.rest import Client
import os

# Load credentials from environment variables
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
RECEIVER_PHONE_NUMBER = os.getenv("RECEIVER_PHONE_NUMBER")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# OpenWeather API endpoint
WEATHER_MAP_API = "https://api.openweathermap.org/data/2.5/forecast"
LAT = 25.0000  # Bermuda Triangle Location
LON = 71.0000
CNT = 4  # 12-hour forecast (each interval is 3 hours)

# API request parameters
parameters = {
    "lat": LAT,
    "lon": LON,
    "cnt": CNT,
    "appid": WEATHER_API_KEY,
}

# Fetch weather data
response = requests.get(url=WEATHER_MAP_API, params=parameters)
response.raise_for_status()
data = response.json()["list"]

# Process weather forecasts
forecasts = [
    {
        "weather_id": item["weather"][0]["id"],
        "weather_description": item["weather"][0]["description"],
    }
    for item in data
]

# Check if it will rain
will_rain = any(forecast["weather_id"] < 700 for forecast in forecasts)

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It is going to rain today. Remember to carry your umbrella!",
        from_=TWILIO_PHONE_NUMBER,
        to=RECEIVER_PHONE_NUMBER,
    )
    print(f"Message sent with status: {message.status}")
