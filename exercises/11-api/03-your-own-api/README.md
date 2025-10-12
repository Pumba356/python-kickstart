# Mini Project 11: Quote API

## Goal

Create your first Flask API that serves inspirational quotes from a JSON data file. This project combines what you've learned about APIs with a practical application of reading data from files.

## Before You Start

**⚠️ IMPORTANT: Complete the exercises first!**

Before attempting this project, make sure you have:
- ✅ Read **Chapter 11: Working with APIs** in the `book/11-api.md` file
- ✅ Completed Exercise 11-01 (Joke Fetcher)
- ✅ Completed Exercise 11-02 (Weather Checker)
- ✅ Created and activated your virtual environment
- ✅ Installed Flask: `pip install flask`

## What You'll Learn

- How to create a simple Flask API
- How to load data from a JSON file
- How to create multiple API endpoints
- How to test your API in a web browser
- How to serve dynamic data through an API

## How It Works

When you run your API server, it will:
1. Load quotes from the `quotes.json` file
2. Start a web server at `http://localhost:5000`
3. Serve quotes through different endpoints
4. Allow you to test it directly in your browser

## 📂 Project Files

This project includes:
- `quotes.json` - Contains 9 inspirational quotes (already created for you!)
- `api_server.py` - Your Flask API (this is what you'll build!)
- `README.md` - This file with instructions

## Step-by-Step Guide

### Step 1: Understanding the Data File

First, take a look at `quotes.json`. Open it and you'll see quotes structured like this:

```json
{
  "quotes": [
    {
      "text": "Code is like humor. When you have to explain it, it's bad.",
      "author": "Cory House",
      "category": "programming"
    }
  ]
}
```

Each quote has three fields: `text`, `author`, and `category`.

### Step 2: Set Up Your Flask App

Open `api_server.py` and start with these imports:

```python
from flask import Flask, jsonify
import json
import random

app = Flask(__name__)
```

### Step 3: Load the Quotes from JSON

**This part is provided for you** - you don't need to understand all the details yet:

```python
# Load quotes from JSON file
with open('quotes.json', 'r') as file:
    data = json.load(file)
    QUOTES = data['quotes']  # Get the list of quotes
```

This code:
- Opens the `quotes.json` file
- Reads the JSON and converts it to a Python dictionary
- Stores the list of quotes in a variable called `QUOTES`

You can copy this code exactly as shown.

### Step 4: Create the Home Page Endpoint

The home page will show users what endpoints are available:

```python
@app.route("/")
def home():
    """Home page with API documentation"""
    return """
    <h1>Welcome to the Quote API!</h1>
    <h2>Available Endpoints:</h2>
    <ul>
        <li><a href="/api/quote">/api/quote</a> - Get a random quote</li>
        <li><a href="/api/quotes">/api/quotes</a> - Get all quotes</li>
    </ul>
    <p>Test the endpoints by clicking the links above!</p>
    """
```

This creates an endpoint at `/` (the home page) that returns HTML.

### Step 5: Create the Random Quote Endpoint

Now create an endpoint that returns a random quote:

```python
@app.route("/api/quote")
def get_random_quote():
    """Get a random quote"""
    # Select a random quote from the list
    random_quote = random.choice(QUOTES)
    return jsonify(random_quote)
```

This:
- Uses `random.choice()` to pick a random quote
- Uses `jsonify()` to convert it to JSON format
- Returns the quote as JSON data

### Step 6: Create the All Quotes Endpoint

Create an endpoint that returns all quotes:

```python
@app.route("/api/quotes")
def get_all_quotes():
    """Get all quotes"""
    return jsonify({
        "total": len(QUOTES),
        "quotes": QUOTES
    })
```

This returns a JSON object with:
- `total`: The number of quotes
- `quotes`: The complete list of quotes

### Step 7: Add the Server Startup Code

Finally, add the code to run the server:

```python
if __name__ == "__main__":
    print("=" * 50)
    print("Quote API Server Started!")
    print("=" * 50)
    print("Open your browser and visit:")
    print("  http://localhost:5000")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 50)
    app.run(debug=True)
```

This:
- Prints helpful information when the server starts
- Runs the Flask development server
- Sets `debug=True` so the server restarts when you make changes

## Running Your API

1. **Make sure you're in the project directory:**
   ```bash
   cd projects/11-api/01-mini-project
   ```

2. **Run the server:**
   ```bash
   python api_server.py
   ```

3. **You should see:**
   ```
   ==================================================
   Quote API Server Started!
   ==================================================
   Open your browser and visit:
     http://localhost:5000
   
   Press Ctrl+C to stop the server
   ==================================================
    * Running on http://127.0.0.1:5000
   ```

4. **Test your API in the browser:**
   - Visit `http://localhost:5000` - See the home page
   - Click on `/api/quote` - Get a random quote
   - Click on `/api/quotes` - See all quotes
   - Refresh the page to get different random quotes

5. **Stop the server:**
   - Press `Ctrl+C` in the terminal

## Expected Output

### Home Page (http://localhost:5000)
You'll see an HTML page with links to the API endpoints.

### Random Quote Endpoint (http://localhost:5000/api/quote)
```json
{
  "text": "First, solve the problem. Then, write the code.",
  "author": "John Johnson",
  "category": "programming"
}
```

### All Quotes Endpoint (http://localhost:5000/api/quotes)
```json
{
  "total": 9,
  "quotes": [
    {
      "text": "Code is like humor...",
      "author": "Cory House",
      "category": "programming"
    },
    ... (8 more quotes)
  ]
}
```

## ✅ Success Criteria

Your project is successful when:
- [ ] Your API server starts without errors
- [ ] You can visit the home page and see the welcome message
- [ ] The `/api/quote` endpoint returns a random quote
- [ ] Refreshing `/api/quote` shows different quotes
- [ ] The `/api/quotes` endpoint returns all 9 quotes
- [ ] The quotes are properly formatted as JSON
- [ ] You can stop the server with Ctrl+C

##  Understanding Flask Decorators

The `@app.route("/path")` syntax is called a **decorator**. It tells Flask:
- What URL path to listen for (e.g., `/api/quote`)
- Which function to run when that path is requested

Think of it like a receptionist directing visitors to different rooms!

## Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
- Make sure your virtual environment is activated
- Install Flask: `pip install flask`

### "FileNotFoundError: quotes.json"
- Make sure you're running the command from the `01-mini-project` directory
- The `quotes.json` file must be in the same folder as `api_server.py`

### "Address already in use"
- Another program is using port 5000
- Stop any other Flask servers you have running
- Or change the port: `app.run(debug=True, port=5001)`

### Browser shows "Unable to connect"
- Make sure the Flask server is still running in the terminal
- Check that you're visiting `http://localhost:5000` (not https)

## Optional Enhancements

Want to make your API even better? Try these ideas:

1. **Add a category filter endpoint:**
   ```python
   @app.route("/api/quote/<category>")
   def get_quote_by_category(category):
       # Filter quotes by category
       filtered = [q for q in QUOTES if q["category"] == category]
       if filtered:
           return jsonify(random.choice(filtered))
       return jsonify({"error": "Category not found"}), 404
   ```

2. **Add a statistics endpoint:**
   ```python
   @app.route("/api/stats")
   def get_stats():
       categories = {}
       for quote in QUOTES:
           cat = quote["category"]
           categories[cat] = categories.get(cat, 0) + 1
       return jsonify({
           "total": len(QUOTES),
           "by_category": categories
       })
   ```

3. **Add more quotes to `quotes.json`**

4. **Create an endpoint that returns only the quote text (no author or category)**

## Concepts Applied

This project demonstrates:
- **Variables** (Chapter 3) → Storing the quotes list
- **Functions** (Chapter 8) → Each endpoint is a function
- **Lists** (Chapter 9) → QUOTES is a list of dictionaries
- **APIs** (Chapter 11) → Creating endpoints and serving JSON data

## What You've Accomplished

By completing this project, you've:
- ✅ Created your first web API with Flask
- ✅ Loaded and used data from a JSON file
- ✅ Created multiple API endpoints
- ✅ Served dynamic data through HTTP
- ✅ Tested APIs in a web browser
- ✅ Learned the basics of web development

This is a huge step! You've created something that could be used by other programs, websites, or mobile apps. Real-world APIs work exactly like this!

##  Next Steps

Congratulations on building your first API! You now understand:
- How to use external APIs (with `requests`)
- How to create your own APIs (with `flask`)
- How JSON data is structured and used
- How web services communicate

**Want to keep learning?**
- Build APIs for other types of data (recipes, movies, books)
- Learn about databases to store data permanently
- Create a web frontend that uses your API
- Explore API authentication and security
- Learn about RESTful API design principles

The world of APIs is huge and exciting - you're just getting started! 🎊