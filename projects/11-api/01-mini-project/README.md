# Mini-Project: Build Your Own API

##  Goal

Your task is to design and build your own simple API using Flask, based on the concepts you learned in Exercise 3 ("Your Own API"). This is an open-ended project, so you have the freedom to choose what your API will do.

The main goal is to practice creating API endpoints and serving data in JSON format.

---

## Requirements

Choose **ONE** of the following paths based on your interests and available hardware:

### Path 1: Data-Driven API (Standard)
Build an API that serves data from a JSON file.

**Your API must have:**
1. **At least 3 different endpoints** (routes)
2. **Data stored in a JSON file** (like `quotes.json` in Exercise 3)
3. **At least one endpoint that returns random data** from your collection
4. **At least one endpoint that returns all items** from your collection
5. **Clear and descriptive endpoint names** (e.g., `/api/movies`, not `/api/data`)

### Path 2: Hardware Control API (Advanced)
Build an API that controls physical electronics through Python.

**Your API must have:**
1. **At least 3 different control endpoints** that interact with hardware
2. **At least one status/sensor endpoint** that returns current hardware state as JSON
3. **Proper error handling** for hardware failures (device not connected, etc.)
4. **Clear endpoint names** describing the action (e.g., `/api/led/on`, `/api/servo/angle/<degrees>`)
5. **Safety features** (timeouts, emergency stop endpoint, value limits)

**Required Hardware & Setup:**
- Raspberry Pi, Arduino, ESP32, or similar microcontroller
- Basic electronic components (LEDs, buttons, sensors, servos, motors, etc.)
- Breadboard and jumper wires
- Python GPIO library installed (`RPi.GPIO`, `gpiozero`, `pySerial`, or similar)
- Basic electronics knowledge (voltage, current, resistors, circuit safety)


---

##  Project Ideas

### Path 1: Data-Driven Projects

Here are some ideas to inspire you. Feel free to choose one of these or create your own!

####  Movie Recommender API
Create an API that recommends movies:
- `/api/movie` - Returns a random movie
- `/api/movies` - Returns all movies
- `/api/movie/genre/<genre>` - Returns a random movie from a specific genre (stretch goal)

**Data example:**
```json
{
  "movies": [
    {"title": "The Matrix", "year": 1999, "genre": "Sci-Fi"},
    {"title": "Inception", "year": 2010, "genre": "Sci-Fi"}
  ]
}
```

###  Song Playlist API
Create an API that serves your favorite songs:
- `/api/song` - Returns a random song
- `/api/songs` - Returns all songs
- `/api/songs/artist/<name>` - Returns songs by a specific artist (stretch goal)

###  Recipe API
Create an API with cooking recipes:
- `/api/recipe` - Returns a random recipe
- `/api/recipes` - Returns all recipes
- `/api/recipes/difficulty/<level>` - Filter by difficulty (stretch goal)

###  Game Tips API
Create an API with gaming tips and tricks:
- `/api/tip` - Returns a random gaming tip
- `/api/tips` - Returns all tips
- `/api/tips/game/<name>` - Tips for a specific game (stretch goal)

###  Book Recommendations API
Create an API for book recommendations:
- `/api/book` - Returns a random book
- `/api/books` - Returns all books
- `/api/books/genre/<genre>` - Filter by genre (stretch goal)

####  Fun Facts API
Create an API with interesting facts:
- `/api/fact` - Returns a random fact
- `/api/facts` - Returns all facts
- `/api/facts/category/<category>` - Filter by category (stretch goal)

---

### Path 2: Hardware Control Projects

If you have electronics hardware, here are some exciting projects:

####  Smart LED Controller API
Control LED lights through your API:
- `/api/led/on` - Turn LED on
- `/api/led/off` - Turn LED off
- `/api/led/toggle` - Toggle LED state
- `/api/led/status` - Returns `{"led": "on"}` or `{"led": "off"}`
- `/api/led/blink?times=5` - Blink LED a specific number of times (stretch goal)

**Hardware needed:** 1 LED, 1 resistor (220Ω), jumper wires

####  Temperature Monitor API
Read and serve temperature sensor data:
- `/api/temperature` - Returns current temperature in JSON
- `/api/temperature/history` - Returns last 10 readings (stored in memory)
- `/api/temperature/alert?threshold=25` - Set temperature alert (stretch goal)

**Hardware needed:** DHT11/DHT22 temperature sensor, jumper wires

####  Traffic Light Controller API
Simulate a traffic light system:
- `/api/traffic/red` - Turn on red LED, others off
- `/api/traffic/yellow` - Turn on yellow LED, others off
- `/api/traffic/green` - Turn on green LED, others off
- `/api/traffic/auto` - Start automatic traffic light sequence
- `/api/traffic/status` - Returns current light state

**Hardware needed:** 3 LEDs (red, yellow, green), 3 resistors, jumper wires

#### 🎵 Buzzer Music API
Control a buzzer to play tones:
- `/api/buzzer/beep?duration=1` - Beep for specified seconds
- `/api/buzzer/tone?frequency=440` - Play a specific frequency
- `/api/buzzer/melody?name=happy_birthday` - Play pre-programmed melody
- `/api/buzzer/stop` - Stop current sound

**Hardware needed:** Active or passive buzzer, jumper wires

####  Servo Motor Controller API
Control a servo motor position:
- `/api/servo/angle/<degrees>` - Move servo to specific angle (0-180)
- `/api/servo/sweep` - Sweep servo back and forth
- `/api/servo/position` - Returns current servo position
- `/api/servo/reset` - Return servo to 0 degrees

**Hardware needed:** Servo motor, external power supply (if needed), jumper wires

####  RGB LED Color API
Control an RGB LED's color:
- `/api/rgb/color?r=255&g=0&b=0` - Set RGB values (0-255 each)
- `/api/rgb/preset/<color_name>` - Set to preset color (red, blue, green, etc.)
- `/api/rgb/rainbow` - Cycle through rainbow colors
- `/api/rgb/off` - Turn off all colors
- `/api/rgb/status` - Returns current RGB values

**Hardware needed:** RGB LED (common cathode or anode), 3 resistors, jumper wires

---

##  Getting Started

### For Path 1 (Data-Driven API):

1. **Choose your topic** - Pick something you're interested in!
2. **Create your data file** - Create a JSON file with at least 5-10 items. Use Exercise 3's `quotes.json` as a template.
3. **Build your Flask API** - Use Exercise 3's `api_server.py` as a starting point and modify it for your data.
4. **Test in your browser** - Visit `http://127.0.0.1:5000/api/...` to see your API in action!

### For Path 2 (Hardware Control API):

1. **Choose your hardware project** - Pick one that matches your available components!
2. **Set up your circuit** - Wire up your components on a breadboard. Double-check connections!
3. **Test hardware separately** - Write a simple Python script to test your hardware works (e.g., blink LED)
4. **Build your Flask API** - Use Exercise 3 as a template, but replace JSON operations with GPIO commands
5. **Add safety features** - Include error handling for hardware failures and safety limits
6. **Test carefully** - Visit `http://127.0.0.1:5000/api/...` in your browser to control your hardware!

---

## 🔧 Path 2: Example Code Structure

Here's a simple example of how to structure a hardware control API (LED controller):

```python
from flask import Flask, jsonify
try:
    import RPi.GPIO as GPIO  # For Raspberry Pi
    # OR: from gpiozero import LED  # Alternative library
except ImportError:
    print("Warning: GPIO library not available. Hardware features disabled.")
    GPIO = None

app = Flask(__name__)

# GPIO Setup
LED_PIN = 17
led_state = False

if GPIO:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)

@app.route("/")
def home():
    return "LED Controller API - Use /api/led/on or /api/led/off"

@app.route("/api/led/on")
def led_on():
    global led_state
    try:
        if GPIO:
            GPIO.output(LED_PIN, GPIO.HIGH)
            led_state = True
            return jsonify({"status": "success", "led": "on"})
        else:
            return jsonify({"status": "error", "message": "GPIO not available"}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/led/off")
def led_off():
    global led_state
    try:
        if GPIO:
            GPIO.output(LED_PIN, GPIO.LOW)
            led_state = False
            return jsonify({"status": "success", "led": "off"})
        else:
            return jsonify({"status": "error", "message": "GPIO not available"}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/led/status")
def led_status():
    return jsonify({"led": "on" if led_state else "off"})

@app.route("/api/emergency/stop")
def emergency_stop():
    """Safety endpoint to turn off all outputs"""
    global led_state
    try:
        if GPIO:
            GPIO.output(LED_PIN, GPIO.LOW)
            led_state = False
            return jsonify({"status": "success", "message": "All outputs disabled"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0')
    finally:
        # Cleanup GPIO on exit
        if GPIO:
            GPIO.cleanup()
```

**Key concepts in this example:**
- Error handling with `try/except` for hardware failures
- Global state tracking (`led_state`)
- Consistent JSON responses with status messages
- Emergency stop endpoint for safety
- GPIO cleanup on program exit

---

##  Tips

### General Tips (Both Paths):
- **Start simple** - Get the basic endpoints working first, then add more features
- **Use descriptive names** - Your endpoints should clearly indicate what they return/do
- **Test frequently** - Run your server and check each endpoint as you build
- **Be creative** - Add your own personality to your API!

### Path 1 Specific Tips:
- **Add more data** - The more items in your JSON file, the more interesting your API becomes
- **Structure your data well** - Think about what information each item should have

### Path 2 Specific Tips:
- **Safety first** - Always double-check your wiring before powering on
- **Use resistors** - Protect your LEDs and Raspberry Pi GPIO pins with appropriate resistors
- **Handle errors gracefully** - GPIO operations can fail; always use try/except blocks
- **Add timeouts** - For operations like motor control, add automatic timeouts
- **Test hardware first** - Make sure your circuit works before integrating with Flask
- **Emergency stop** - Include a `/api/emergency/stop` endpoint that safely shuts down all outputs

---

## Stretch Goals (Optional)

If you finish early and want to challenge yourself:

### Path 1 Stretch Goals:
1. **Add filtering** - Create endpoints that filter data by a specific property (like genre, year, difficulty)
2. **Add a counter** - Track how many times each endpoint has been accessed
3. **Add timestamps** - Include the current time when returning data
4. **Add search** - Create an endpoint that searches through your data
5. **Create a simple HTML page** - Make a webpage that displays data from your API using JavaScript

### Path 2 Stretch Goals:
1. **Add sensor fusion** - Combine multiple sensors (e.g., temperature + humidity)
2. **Add scheduling** - Create endpoints that schedule hardware actions (e.g., turn on LED in 10 seconds)
3. **Add PWM control** - Use PWM for LED brightness or motor speed control
4. **Create patterns** - Pre-program sequences (e.g., traffic light patterns, LED light shows)
5. **Add a web dashboard** - Create a simple HTML page with buttons to control hardware
6. **Data logging** - Store sensor readings to a file with timestamps

---

## ✅ Checklist

### Path 1 Checklist:
Before you consider your project complete, make sure you have:

- [ ] Created a JSON file with your data (at least 5 items)
- [ ] Built a Flask API with at least 3 endpoints
- [ ] One endpoint returns a random item
- [ ] One endpoint returns all items
- [ ] Tested all endpoints in your browser
- [ ] Your code is clean and uses descriptive variable names
- [ ] You understand how each part of your code works

### Path 2 Checklist:
Before you consider your project complete, make sure you have:

- [ ] Set up your hardware circuit correctly and safely
- [ ] Tested hardware separately before integrating with Flask
- [ ] Built a Flask API with at least 3 control endpoints
- [ ] At least one endpoint returns sensor/status data as JSON
- [ ] Implemented error handling for hardware failures
- [ ] Added safety features (timeouts, limits, emergency stop)
- [ ] Tested all endpoints in your browser
- [ ] Your circuit is properly documented (you can rebuild it)
- [ ] Your code is clean and uses descriptive variable names
- [ ] You understand how each part of your code works

---

## 🎉 Have Fun!

This is your chance to build something creative! Think about what you'd like to use an API for, and build it. Remember, the best way to learn is by doing, so don't be afraid to experiment and try new things!

When you're done, you can show your API to your classmates and see what they built too!