"""
Exercise 11-01: Joke Fetcher - Solution
Fetch and display a random Chuck Norris joke from an API
"""

import requests

# API endpoint
url = "https://api.chucknorris.io/jokes/random"

# Make GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # Extract and display the joke
    print(data["value"])
else:
    print(f"Error: Failed to fetch joke (Status code: {response.status_code})")