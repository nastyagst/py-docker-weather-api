import os
import requests
import sys


def get_weather():
    api_key = os.getenv("API_KEY")
    city = "Paris"

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        sys.exit(1)

    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Current weather in {city}: {condition}, {temp}°C")
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()