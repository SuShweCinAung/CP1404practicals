try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

"""
Answers:
1. A ValueError will occur when the user gives an alphabet as an input
2. A ZeroDivisionError will occur when the user puts a zero as an input for denominator
3. Yes, it could avoid the possibility of a ZeroDivisionError
"""