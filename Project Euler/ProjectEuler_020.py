# ProjectEuler_020

'''
n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

# Using the math package function for the factorial.
import math

# Summing all the digits from 100!
print(sum(int(digit) for digit in str(math.factorial(100))))

# The sum of the digits in the number 100! is 648.