# ProjectEuler_002

# Start Date : 2/22/2023
# Solved Date: 2/24/2023

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# I might modify this code to be a function with an input instead.

# Defining the first two terms, and the sum of the even-valued terms which we will find later.
a, b = 0, 1
fibSum = 0

# The current iteration's b will become next iteration's a, and current iteration's a + b will become next iteration's b.
# The code will stop after b exceeds 4000000
# The line after sums the even-valued terms of the sequence if the remainder after dividing b by 2 equals zero.
while True:
    a, b = b, a + b
    if b > 4000000:
        break
    if b % 2 == 0:
        fibSum += b

print(fibSum)

# The sum of the even-valued terms is 4613732.