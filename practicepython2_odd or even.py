# Practice Python Exercise 2
# Odd or Even
# This program determines the parity of a number using the modulus operation.

print('Enter a number. The program will determine whether the number is odd or even.')
number = int(input())
mod2 = number % 2
mod4 = number % 4
if mod4 == 0:
    print(str(number) + ' is an even number. It is also divisible by 4.')
elif mod2 == 0:
    print(str(number) + ' is an even number.')
else:
    print(str(number) + ' is an odd number.')
