#!/usr/bin/python3
def remove_char_at(input_str, n):
    if n < 0 or n >= len(input_str):
        return input_str  # Return the original string if n is out of bounds

    # Create a new string without the character at position n
    result = input_str[:n] + input_str[n+1:]
    
    return result

# Test the function
original_str = "Python"
n = 2
new_str = remove_char_at(original_str, n)
print(new_str)  # Output: "Pyhon"
