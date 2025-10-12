"""
Mini Project 11: Quote API - Solution
Flask API that serves inspirational quotes from a JSON file
"""

from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

# Load quotes from JSON file
# This code reads the quotes.json file and converts it to a Python dictionary
# You don't need to change this part - it's provided for you!
with open('quotes.json', 'r') as file:
    data = json.load(file)
    QUOTES = data['quotes']  # Get the list of quotes from the JSON

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

@app.route("/api/quote")
def get_random_quote():
    """Get a random quote"""
    # Select a random quote from the list
    random_quote = random.choice(QUOTES)
    return jsonify(random_quote)

@app.route("/api/quotes")
def get_all_quotes():
    """Get all quotes"""
    return jsonify({
        "total": len(QUOTES),
        "quotes": QUOTES
    })

if __name__ == "__main__":
    print("=" * 50)
    print("Quote API Server Started!")
    print("=" * 50)
    print("Open your browser and visit:")
    print("  http://localhost:5000")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 50)
    app.run(debug=True)