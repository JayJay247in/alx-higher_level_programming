#!/usr/bin/python3
def print_last_digit(number):
    # Calculate the last digit using modulo operator
    last_digit = abs(number) % 10
    
    # Print the last digit
    print(last_digit)
    
    # Return the last digit's value
    return last_digit

# Test the function
result = print_last_digit(12345)
print("Last digit:", result)
