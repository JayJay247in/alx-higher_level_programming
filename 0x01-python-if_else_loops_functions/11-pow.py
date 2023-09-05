#!/usr/bin/python3
def pow(a, b):
    result = 1

    if b < 0:
        a = 1 / a
        b = -b

    for _ in range(b):
        result *= a

    return result

# Test the function
print(pow(2, 3))  # Output: 8
print(pow(5, -2)) # Output: 0.04
