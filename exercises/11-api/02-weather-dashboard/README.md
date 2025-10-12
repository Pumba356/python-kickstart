# Exercise 11-02: Weather Checker

## Background

The Open-Meteo API provides free weather data for locations worldwide. In this exercise, you will write a program that fetches the current weather for Stockholm.

## Before You Start

**IMPORTANT: Complete Exercise 1 first!**

Before attempting this exercise, make sure you have:
- Completed Exercise 11-01 (Joke Fetcher)
- Understood how to make API requests and check status codes
- Understood how to work with dictionaries (from Exercise 1)
- Your virtual environment is still activated
- The `requests` library is installed

## Goal

Create a program that fetches current weather data for Stockholm from the Open-Meteo API and displays the temperature and wind speed.

## What You'll Learn

This exercise builds on Exercise 1 by introducing two new concepts:
- How to pass **query parameters** to an API request
- How to work with **nested dictionary data**

## Instructions

Build your program step by step. You already know how to do most of this from Exercise 1!

1. **Import the requests library** (just like in Exercise 1)

2. **Set up the API URL and parameters**
   - URL: `https://api.open-meteo.com/v1/forecast`
   - Parameters: See the hint below for how to create a params dictionary

3. **Make the GET request** (just like in Exercise 1, but this time pass the `params`)

4. **Check if the request was successful** (remember `response.status_code == 200` from Exercise 1?)

5. **Convert the response to a dictionary** (you did this in Exercise 1 with `response.json()`)

6. **Extract the weather data** (this is the new part - see hints below!)

7. **Display the weather information** (use `print()` with f-strings)

## Hints

### New Concept 1: Passing Parameters

Some APIs need additional information (called **query parameters**). For this API, we need to tell it which location we want weather for.

Create a dictionary with the parameters:
```python
params = {
    "latitude": 59.33,
    "longitude": 18.07,
    "current_weather": True
}
```

Then pass it to `requests.get()`:
```python
response = requests.get(url, params=params)
```

### New Concept 2: Nested Dictionaries

The weather data is **nested** inside the response. Think of it like a dictionary inside a dictionary:

```python
# First, get the main data (just like Exercise 1)
data = response.json()

# Then, get the weather information from inside
weather = data["current_weather"]

# Now you can get specific values
temperature = weather["temperature"]
windspeed = weather["windspeed"]
```

### What You Already Know

- How to import `requests` ✓
- How to make a GET request ✓
- How to check `response.status_code` ✓
- How to use `response.json()` ✓
- How to access dictionary values with `data["key"]` ✓

You just need to apply these skills with the two new concepts!

## Expected Output

When you run your program, you should see something like:
```
Weather in Stockholm:
Temperature: 15.2°C
Wind Speed: 12.5 km/h
```

(Note: The actual values will vary based on current weather conditions)

## Challenge: Add More Information

Once your basic program works, try this modification:

**Display the wind direction:** The weather data also includes `winddirection` in degrees. Modify your code to display it.

Your final output should look like this:
```
Weather in Stockholm:
Temperature: 15.2°C
Wind Speed: 12.5 km/h
Wind Direction: 270°
```

**Hint:** Just like you accessed `weather["temperature"]`, you can also access `weather["winddirection"]`.

## Success!

Once your program works, you've successfully:
- Applied what you learned in Exercise 1 to a new API
- Passed query parameters to customize an API request
- Worked with nested dictionary data
- Extracted multiple values from an API response

Ready for the mini-project where you'll build your own API? Excellent work!