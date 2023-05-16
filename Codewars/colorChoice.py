# Color Choice
# https://www.codewars.com/kata/55be10de92aad5ef28000023

import math

def checkchoose(x, m):

    # Check for negatives
    if x < 0 or m < 0 or x > math.factorial(m):
        return(-1)

    # Rearrange the formula for combination, iterate until m
    for n in range(m + 1):
        result = (math.factorial(m)) // (math.factorial(n) * math.factorial(m - n))
        if result == x:
            return n

    # If n is not found    
    return(-1)

print(checkchoose(35,7))