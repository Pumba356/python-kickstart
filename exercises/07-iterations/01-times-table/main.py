#!/usr/bin/env python3
"""
Exercise 1: Times Table Generator

Generate multiplication tables using for loops.
"""

# Write your code here
# 1. Ask user for a number
# 2. Print a header for the times table
# 3. Use a for loop with range(1, 11) to generate table
# 4. Calculate and print each multiplication result
number = int(input("Please enter a number for the times table: "))
print(f"\nTimes Table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")