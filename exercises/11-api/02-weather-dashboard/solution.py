"""
Exercise 11-02: Weather Checker - Solution
Fetch current weather for Stockholm
"""

import requests

# API endpoint
url = "https://api.open-meteo.com/v1/forecast"

# Parameters for Stockholm
params = {
    "latitude": 59.33,
    "longitude": 18.07,
    "current_weather": True
}

# Make GET request
response = requests.get(url, params=params)

# Check if request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    weather = data["current_weather"]
    
    # Display weather information
    print("Weather in Stockholm:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Wind Speed: {weather['windspeed']} km/h")
else:
    print(f"Error: Failed to fetch weather data (Status code: {response.status_code})")