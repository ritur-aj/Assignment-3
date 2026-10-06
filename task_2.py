# Task 2: Using the Math Module for Calculations
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
    # o   Square root of the number
    # o   Natural logarithm (log base e) of the number
    # o   Sine of the number (in radians)
# 3.   Displays the calculated results.

import math

number = float(input("Enter a number: "))

square_root = math.sqrt(number)
natural_log = math.log(number)
sine = math.sin(number)

print(f"Square root of {number}: {square_root :.2f}")
print(f"Natural logarithm of {number}: {natural_log :.2f}")
print(f"Sine of {number} radians: {sine :.2f}")