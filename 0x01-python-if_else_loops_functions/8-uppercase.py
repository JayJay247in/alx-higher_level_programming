#!/usr/bin/python3
def uppercase(s):
    result = ""
    
    for char in s:
        if 'a' <= char <= 'z':
            # Convert lowercase letter to uppercase using ASCII values
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            # Keep non-lowercase letters unchanged
            result += char
    
    # Print the result in uppercase followed by a new line
    print(result)

# Test the function
uppercase("Hello, World!")  # Output: "HELLO, WORLD!"
