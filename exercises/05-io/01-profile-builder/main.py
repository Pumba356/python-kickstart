#!/usr/bin/env python3
"""
Exercise 1: Personal Profile Builder

Create an interactive program that collects user information 
and displays a formatted profile.
"""

# Write your code here
# 1. Print a welcome message
# 2. Ask for name, age, height, and hobby using input()
# 3. Convert age to int and height to float
# 4. Calculate birth year (2024 - age)
# 5. Display formatted profile using f-strings
print("Welcome to the Personal Profile Builder!")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
hobby = input("Please enter your favorite hobby: ")
birth_year = 2024 - age
print(f"\n--- Your Profile ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} m")
print(f"Hobby: {hobby}")
print(f"Birth Year: {birth_year}")