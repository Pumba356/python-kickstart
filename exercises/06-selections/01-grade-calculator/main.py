#!/usr/bin/env python3
"""
Exercise 1: Grade Calculator

Convert numeric scores to letter grades with feedback.
"""

# Write your code here
# 1. Ask user for a score (0-100)
# 2. Convert score to letter grade using if/elif/else:
#    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59
# 3. Provide appropriate feedback for each grade
# 4. Display the grade and feedback
score = float(input("Please enter your score (0-100): "))
if score >= 90:
    grade = 'A'
    feedback = "Excellent work!"
elif score >= 80:
    grade = 'B'
    feedback = "Good job!"
elif score >= 70:
    grade = 'C'
    feedback = "Satisfactory."
elif score >= 60:
    grade = 'D'
    feedback = "Needs improvement."
else:
    grade = 'F'
    feedback = "Failed. Please try again."
print(f"Grade: {grade}")
print(f"Feedback: {feedback}")