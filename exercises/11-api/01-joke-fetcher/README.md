# Exercise 11-01: Joke Fetcher

## Background

The Chuck Norris API provides random jokes about Chuck Norris. You will use the `requests` library to fetch and display jokes from this free API.

## Before You Start

**⚠️ IMPORTANT: Read Chapter 11 first!**

Before attempting this exercise, make sure you have:
- Read **Chapter 11: Working with APIs** in the `book/11-api.md` file
- Understood how APIs work and what JSON is
- Created and activated your virtual environment
- Installed the `requests` library: `pip install requests`

## Goal

Create a program that fetches a random Chuck Norris joke from an API and displays it.

## What You'll Learn

- How to make your first API request using the `requests` library
- How to check if a request was successful
- How to work with JSON data (which gets converted to a Python dictionary)
- How to extract specific information from API responses

## Step-by-Step Instructions

Follow these steps to build your program:

### Step 1: Import the requests library

```python
import requests
```

### Step 2: Define the URL and make the request

```python
url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
```

### Step 3: Check if the request was successful

Use an `if` statement to check the `status_code`. A code of `200` means success.

```python
if response.status_code == 200:
    # The request worked! Continue here...
else:
    print(f"Error: Unable to fetch joke. Status code: {response.status_code}")
```

### Step 4: Get the data and extract the joke

Inside the `if` block, convert the JSON response to a Python dictionary and get the joke.

**Important:** `response.json()` converts the JSON data into a Python **dictionary**. A dictionary is like a contact list where you look up information using a key (like a name) to get a value (like a phone number).

```python
data = response.json()  # Converts JSON to a dictionary
joke = data['value']    # Get the joke text using the key 'value'
```

### Step 5: Display the joke

```python
print(joke)
```

## Expected Output

When you run your program, you should see something like:
```
Chuck Norris can divide by zero.
```

(Note: The joke will be different each time you run the program)

## Challenge: Make It Your Own

Once your basic program works, try this modification:

**Display more information:** Modify your code to also print the `id` of the joke and the `url` where the joke can be found online.

Your final output should look something like this:
```
Joke: Chuck Norris can divide by zero.
ID: R_aAY3DkS8m-Qq_So4925A
URL: https://api.chucknorris.io/jokes/R_aAY3DkS8m-Qq_So4925A
```

**Hint:** Just like you accessed `data['value']`, you can also access `data['id']` and `data['url']`.

## Understanding Dictionaries

When you use `response.json()`, you get back a **dictionary**. Think of it like this:

```python
# A dictionary is like a phonebook:
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678"
}

# You look up values using keys:
alice_number = phonebook["Alice"]  # Returns "555-1234"
```

The API response works the same way:
```python
data = response.json()  # Returns something like:
# {
#   "value": "Chuck Norris can divide by zero.",
#   "id": "R_aAY3DkS8m-Qq_So4925A",
#   "url": "https://api.chucknorris.io/jokes/..."
# }

joke = data["value"]  # Gets the joke text
```

## Success!

Once your program works, you've successfully:
- Made your first API request
- Checked response status codes
- Worked with JSON data and Python dictionaries
- Extracted information using dictionary keys

Ready for Exercise 2? Great work!