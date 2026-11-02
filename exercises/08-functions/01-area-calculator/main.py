# Exercise 1: Area Calculator Functions
# Practice defining and using functions for mathematical calculations

# TODO: Define your area calculation functions here

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle"""
    # TODO: Calculate and return length * width
    pass

def calculate_circle_area(radius):
    """Calculate the area of a circle"""
    # TODO: Calculate and return π * radius²
    # Use 3.14159 for π
    pass

def calculate_triangle_area(base, height):
    """Calculate the area of a triangle"""
    # TODO: Calculate and return (base * height) / 2
    pass

# TODO: Use your functions to calculate areas
print("=== Area Calculator ===")

# Test your functions with these values:
# Rectangle: length=5, width=3
# Circle: radius=4
# Triangle: base=6, height=8

# Example of how to call a function (uncomment and complete):
# rectangle_area = calculate_rectangle_area(5, 3)
# print(f"Rectangle (5 × 3): {rectangle_area} square units")

# TODO: Add calls for circle and triangle calculations
circle_area = calculate_circle_area(4)
triangle_area = calculate_triangle_area(6, 8)
print(f"Circle (radius 4): {circle_area} square units")
print(f"Triangle (6 × 8): {triangle_area} square units")
