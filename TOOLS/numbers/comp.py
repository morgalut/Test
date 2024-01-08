import random

def sum_of_digits_for_larger_number(num1: int, num2: int) -> int:
    """
    Calculate the sum of digits for the larger of two given numbers.

    Parameters:
    - num1 (int): The first input integer.
    - num2 (int): The second input integer.

    Returns:
    - int: The sum of digits for the larger number.
    """
    larger_number = max(num1, num2)
    return sum(int(digit) for digit in str(abs(larger_number)))

def is_palindrome(number: int) -> bool:
    """
    Check if a given number is a palindrome.

    Parameters:
    - number (int): The input integer.

    Returns:
    - bool: True if the number is a palindrome, False otherwise.
    """
    try:
        str_number = str(abs(number))
        return str_number == str_number[::-1]
    except ValueError:
        return False  # Non-integer values are not palindromes.

def is_palindrome_for_random_numbers() -> bool:
    """
    Check if a randomly generated number is a palindrome.

    Returns:
    - bool: True if the number is a palindrome, False otherwise.
    """
    random_number1 = random.randint(100, 999)
    random_number2 = random.randint(100, 999)
    
    # Display the larger of the two random numbers
    larger_random_number = max(random_number1, random_number2)
    print(f"Generated numbers: {random_number1}, {random_number2}")
    print("Larger number:", larger_random_number)

    return is_palindrome(larger_random_number)

# Use the is_palindrome_for_random_numbers function
result_is_palindrome = is_palindrome_for_random_numbers()
print(f"Is palindrome for the larger randomly generated number: {result_is_palindrome}")

# comp.py

def another_function():
    print("Executing another_function in comp.py")
