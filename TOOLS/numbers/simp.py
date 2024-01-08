# File: TOOLS/SIMP.py

def add_two_numbers(a, b):
    return a + b

def subtract_two_numbers(a, b):
    return a - b

# Take user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform addition and subtraction using the input numbers
result_add = add_two_numbers(num1, num2)
result_subtract = subtract_two_numbers(num1, num2)

# Display the results
print("Result of adding:", result_add)
print("Result of subtracting:", result_subtract)
# simp.py

class SomeClass:
    def some_method(self):
        print("Executing some_method in SomeClass from simp.py")

