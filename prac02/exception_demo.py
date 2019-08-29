"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?: When the user puts in anything other than a whole number
2. When will a ZeroDivisionError occur?: When the user puts in a 0 for the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError? NO
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
