# Chapter 11: Working with APIs in Python

## Learning Objectives

By the end of this chapter, you will be able to:
- Understand what APIs are and why they're important in modern programming
- Use the `requests` library to fetch data from external APIs
- Parse JSON responses and extract useful information
- Create your own API using Flask
- Build applications that combine data from multiple sources
- Handle API errors and edge cases appropriately

## Introduction

**API** stands for **Application Programming Interface**. While that sounds technical, the concept is simple: an API is a way for programs to talk to each other and share data.

### The Restaurant Menu Analogy

Think of an API like a restaurant menu:

- **The Menu**: Lists what you can order (available endpoints)
- **Your Order**: The request you make (GET, POST, etc.)
- **The Kitchen**: The server that processes your request (backend)
- **Your Food**: The response you receive (usually JSON data)

You don't need to know how the kitchen works. You just need to know what's on the menu and how to order. That's exactly how APIs work.

### Real-World Examples

APIs power most of the internet:

- **Spotify**: Music apps use Spotify's API to play songs
- **Google Maps**: Delivery apps use Maps API to show routes
- **Weather Services**: Your phone's weather app fetches data from weather APIs
- **Social Media**: Apps use Twitter/Instagram APIs to post content
- **Payment Systems**: Online stores use payment APIs to process transactions

### How APIs Work

Most modern APIs use **REST** (Representational State Transfer) and communicate over **HTTP**:

1. **Request**: Your program sends a request to a URL (endpoint)
2. **Processing**: The server processes your request
3. **Response**: The server sends back data (usually in JSON format)

```python
# Simple API flow
import requests

# 1. Make request to API
response = requests.get("https://api.example.com/data")

# 2. Get data from response
data = response.json()

# 3. Use the data
print(data)
```

## Core Concepts

### Installing Required Packages

Before working with APIs, create and activate a virtual environment (as you learned in Chapter 10):

```bash
# Create and activate venv
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or .venv\Scripts\Activate.ps1 on Windows

# Install requests library
pip install requests
```

### Using External APIs

Let's start with a simple example using the Chuck Norris API:

```python
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
    print(f"Error: {response.status_code}")
```

Output (random each time):
```
Chuck Norris can divide by zero.
```

### Understanding the Response Object

The `requests.get()` function returns a Response object with useful properties:

```python
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

# Status code (200 = success)
print(f"Status Code: {response.status_code}")

# Response headers
print(f"Content Type: {response.headers['content-type']}")

# Raw text
print(f"Raw Response: {response.text}")

# Parsed JSON (as Python dictionary)
data = response.json()
print(f"JSON Data: {data}")

# Check if successful
if response.ok:  # True if status code is < 400
    print("Request successful!")
```

### Working with JSON Data

JSON (JavaScript Object Notation) is the standard format for API data. Python's `requests` library automatically converts JSON to Python dictionaries:

```python
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()

# JSON is converted to a Python dictionary
print(f"Type: {type(data)}")  # <class 'dict'>

# Access values using dictionary keys
joke_id = data["id"]
joke_text = data["value"]
joke_url = data["url"]

print(f"ID: {joke_id}")
print(f"Joke: {joke_text}")
print(f"URL: {joke_url}")
```

### API with Query Parameters

Many APIs accept parameters to customize requests. Let's use the Open-Meteo weather API:

```python
import requests

# API endpoint with query parameters
url = "https://api.open-meteo.com/v1/forecast"

# Parameters as dictionary
params = {
    "latitude": 59.33,   # Stockholm coordinates
    "longitude": 18.07,
    "current_weather": True
}

# Send request with parameters
response = requests.get(url, params=params)

if response.ok:
    data = response.json()
    weather = data["current_weather"]
    
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Wind Speed: {weather['windspeed']} km/h")
    print(f"Weather Code: {weather['weathercode']}")
else:
    print(f"Error: {response.status_code}")
```

### Creating Interactive API Programs

Combine user input with API calls:

```python
import requests

def get_weather_for_city():
    # City coordinates (simplified example)
    cities = {
        "stockholm": (59.33, 18.07),
        "gothenburg": (57.71, 11.97),
        "malmo": (55.61, 13.00)
    }
    
    print("Available cities:")
    for city in cities.keys():
        print(f"- {city.capitalize()}")
    
    city_name = input("\nEnter city name: ").lower()
    
    if city_name in cities:
        lat, lon = cities[city_name]
        
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }
        
        response = requests.get(url, params=params)
        
        if response.ok:
            weather = response.json()["current_weather"]
            print(f"\nWeather in {city_name.capitalize()}:")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Wind Speed: {weather['windspeed']} km/h")
        else:
            print(f"Error fetching weather data: {response.status_code}")
    else:
        print("City not found in database")

# Run the program
get_weather_for_city()
```

## Building Your Own API with Flask

Now let's create our own API using Flask, a lightweight web framework:

### Installing Flask

```bash
# Make sure your venv is activated
pip install flask
```

### Your First Flask API

Create a file called `app.py`:

```python
from flask import Flask, jsonify

# Create Flask application
app = Flask(__name__)

# Define a route (endpoint)
@app.route("/")
def home():
    return "Welcome to my first API!"

# JSON endpoint
@app.route("/api/hello")
def hello():
    return jsonify({
        "message": "Hello from your first API!",
        "status": "success"
    })

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```

Run the application:

```bash
python app.py
```

Visit in your browser:
- http://localhost:5000/ - See welcome message
- http://localhost:5000/api/hello - See JSON response

### Creating Dynamic Endpoints

Add endpoints that process data:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Math API!"

# Addition endpoint using query parameters
@app.route("/api/add")
def add_numbers():
    # Get query parameters
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    
    if a is None or b is None:
        return jsonify({
            "error": "Please provide both 'a' and 'b' parameters",
            "example": "/api/add?a=5&b=3"
        }), 400
    
    result = a + b
    return jsonify({
        "a": a,
        "b": b,
        "sum": result
    })

# Random quote endpoint
@app.route("/api/quote")
def random_quote():
    import random
    
    quotes = [
        "Code is like humor. When you have to explain it, it's bad.",
        "First, solve the problem. Then, write the code.",
        "Simplicity is the soul of efficiency."
    ]
    
    quote = random.choice(quotes)
    return jsonify({
        "quote": quote,
        "count": len(quotes)
    })

if __name__ == "__main__":
    app.run(debug=True)
```

Test the endpoints:
- http://localhost:5000/api/add?a=5&b=3 - Returns sum
- http://localhost:5000/api/quote - Returns random quote

### Using Path Parameters

Flask also supports URL path parameters:

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Path parameter example
@app.route("/api/user/<username>")
def get_user(username):
    return jsonify({
        "username": username,
        "message": f"Welcome, {username}!"
    })

# Multiple path parameters
@app.route("/api/multiply/<int:a>/<int:b>")
def multiply(a, b):
    return jsonify({
        "a": a,
        "b": b,
        "product": a * b
    })

if __name__ == "__main__":
    app.run(debug=True)
```

Test these endpoints:
- http://localhost:5000/api/user/alice
- http://localhost:5000/api/multiply/7/8

### Consuming Your Own API

Create a separate Python script to fetch data from your Flask API:

**client.py:**
```python
import requests

# Make sure your Flask app is running first!

def test_api():
    base_url = "http://localhost:5000"
    
    # Test addition endpoint
    print("Testing addition endpoint...")
    response = requests.get(f"{base_url}/api/add?a=10&b=5")
    if response.ok:
        data = response.json()
        print(f"{data['a']} + {data['b']} = {data['sum']}")
    
    # Test quote endpoint
    print("\nTesting quote endpoint...")
    response = requests.get(f"{base_url}/api/quote")
    if response.ok:
        data = response.json()
        print(f"Quote: {data['quote']}")
    
    # Test user endpoint
    print("\nTesting user endpoint...")
    username = input("Enter your name: ")
    response = requests.get(f"{base_url}/api/user/{username}")
    if response.ok:
        data = response.json()
        print(data["message"])

# Run the client
test_api()
```

## Practical Example: Combined API Application

Here's a complete example that creates a Flask API and uses external APIs:

**weather_api.py:**
```python
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Weather Aggregator API - Use /api/weather?city=stockholm"

@app.route("/api/weather")
def get_weather():
    # City coordinates database
    cities = {
        "stockholm": {"lat": 59.33, "lon": 18.07},
        "gothenburg": {"lat": 57.71, "lon": 11.97},
        "malmo": {"lat": 55.61, "lon": 13.00}
    }
    
    city = request.args.get("city", "").lower()
    
    if city not in cities:
        return jsonify({
            "error": "City not found",
            "available_cities": list(cities.keys())
        }), 404
    
    # Fetch weather from external API
    coords = cities[city]
    weather_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": coords["lat"],
        "longitude": coords["lon"],
        "current_weather": True
    }
    
    response = requests.get(weather_url, params=params)
    
    if response.ok:
        weather_data = response.json()["current_weather"]
        return jsonify({
            "city": city.capitalize(),
            "temperature": weather_data["temperature"],
            "windspeed": weather_data["windspeed"],
            "units": {
                "temperature": "°C",
                "windspeed": "km/h"
            }
        })
    else:
        return jsonify({
            "error": "Failed to fetch weather data"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
```

## Error Handling

Always handle potential errors when working with APIs:

```python
import requests

def safe_api_call(url):
    try:
        response = requests.get(url, timeout=5)  # 5 second timeout
        response.raise_for_status()  # Raise exception for 4xx/5xx status codes
        return response.json()
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Use the safe function
data = safe_api_call("https://api.chucknorris.io/jokes/random")
if data:
    print(data["value"])
else:
    print("Failed to fetch joke")
```

## Common Mistakes

### Forgetting to Check Status Codes

```python
import requests

# Wrong - assuming request always succeeds
response = requests.get("https://api.example.com/data")
data = response.json()  # Might fail if status code is 404!

# Correct - check status first
response = requests.get("https://api.example.com/data")
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### Not Using Virtual Environments

```bash
# Wrong - installing globally
pip install flask requests

# Correct - use venv
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1
pip install flask requests
```

### Hardcoding API Keys in Code

```python
# Wrong - exposing sensitive data
api_key = "sk_live_abc123xyz789"  # Never do this!
url = f"https://api.service.com/data?key={api_key}"

# Correct - use environment variables
import os
api_key = os.environ.get("API_KEY")
if api_key:
    url = f"https://api.service.com/data?key={api_key}"
```

### Not Handling Network Errors

```python
# Wrong - no error handling
response = requests.get(url)
data = response.json()

# Correct - handle potential errors
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

## Practice

Try these exercises to practice what you've learned:

1. **Joke Fetcher**: Create a program that fetches and displays jokes from the Chuck Norris API
2. **Weather Dashboard**: Build an interactive weather program that lets users check weather for different cities
3. **Your Own API**: Create a Flask API that serves inspirational quotes from a JSON file

## Mini-Project

Once you've completed the exercises, challenge yourself with the **Mini-Project: Build Your Own API**. This is an open-ended project where you design and create your own unique API using what you learned in Exercise 3. You could build:
- A movie recommender API
- A recipe API
- A gaming tips API
- Or anything else you find interesting!

The mini-project lets you be creative while practicing the skills you've learned.

## Optional Extensions

### POST Requests

While GET requests retrieve data, POST requests send data to APIs:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
tasks = []

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    
    if "task" not in data:
        return jsonify({"error": "Missing 'task' field"}), 400
    
    tasks.append(data["task"])
    return jsonify({
        "message": "Task added",
        "task": data["task"],
        "total": len(tasks)
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
```

Test with Python:
```python
import requests

# Add a task
response = requests.post(
    "http://localhost:5000/api/tasks",
    json={"task": "Learn Python APIs"}
)
print(response.json())

# Get all tasks
response = requests.get("http://localhost:5000/api/tasks")
print(response.json())
```

### Testing APIs with Tools

**Postman** and **curl** are useful tools for testing APIs:

```bash
# Using curl to test your API
curl http://localhost:5000/api/hello

# POST request with curl
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"task": "Learn APIs"}'
```

## Summary

In this chapter, you learned:

- APIs enable programs to communicate and share data
- The `requests` library makes it easy to fetch data from external APIs
- JSON is the standard format for API data, which Python handles as dictionaries
- Flask allows you to create your own APIs with simple Python code
- Always handle errors when working with APIs
- Virtual environments are essential for managing API-related packages
- GET requests retrieve data, while POST requests send data

APIs are fundamental to modern software development. They allow you to:
- Integrate with external services (weather, maps, payments)
- Build microservices that work together
- Create mobile and web apps with separated frontend/backend
- Share data between different programs and platforms

With these skills, you can now build applications that connect to the wider internet ecosystem and create your own services that others can use.

## Quick Reference

### Making API Requests

```python
import requests

# GET request
response = requests.get("https://api.example.com/data")

# GET with parameters
params = {"key": "value", "limit": 10}
response = requests.get("https://api.example.com/data", params=params)

# POST request
data = {"name": "Alice", "age": 25}
response = requests.post("https://api.example.com/users", json=data)

# Check response
if response.ok:
    data = response.json()
    print(data)
```

### Creating Flask APIs

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/endpoint")
def endpoint():
    return jsonify({"message": "Hello!"})

@app.route("/api/user/<username>")
def get_user(username):
    return jsonify({"user": username})

if __name__ == "__main__":
    app.run(debug=True)
```

### Checklist for API Projects

- [ ] Create and activate virtual environment
- [ ] Install required packages (`requests`, `flask`)
- [ ] Test API endpoints before using them
- [ ] Check response status codes
- [ ] Handle errors gracefully
- [ ] Never hardcode API keys in your code
- [ ] Use meaningful variable names
- [ ] Add timeout to requests
- [ ] Document your API endpoints

Now you have the tools to both consume and create APIs. In your future projects, you'll find APIs invaluable for accessing data and building connected applications!