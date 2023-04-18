# ProjectEuler_006

'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
'''

# Sum of squares
SumOfSquares = 0
for i in range (1,101):
    SumOfSquares = SumOfSquares + i ** 2
    i += 1
print(SumOfSquares)

# Square of sum
print((sum(range(1,101)))**2)

# Subtract square of sum by sum of squares
answer = ((sum(range(1,101)))**2) - SumOfSquares
print(answer)

# The difference is 25164150.