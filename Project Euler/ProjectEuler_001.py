# ProjectEuler_001

# Start Date : 2/22/2023
# Solved Date: 2/22/2023

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# First, we calculate the sum of all the numbers below 1000 that are divisible by 3, and then the ones divisible by 5.
div3  = (sum(range(3,1000,3)))
div5  = (sum(range(5,1000,5)))

# And then we calculate the sum of all the numbers below 1000 that are divisible by both 3 and 5, or in other words divisible by 15.
div15 = (sum(range(15,1000,15)))

# The sum of each group of numbers displayed
print(div3)
print(div5)
print(div15)

# To find the sum of all the multiples of 3 OR 5 below 1000, we just have to add div3 and div5, and then subtract by div15.
print(div3 + div5 - div15)

# The sum of all the multiples of 3 or 5 below 1000 is 233168.