# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:03:00 2022

@author: Lenovo
"""

'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

# I need to make the code repeat itself and show an error message if it receives an invalid input.
print('Divisors')
n = int(input('Input a nonnegative integer: '))
div = []

if n >= 2:
    numbers = list(range(2,(n+1)))
    for i in numbers:
        if n % i == 0:
            div.append(i)
        else:
            continue
    print(div)
elif n == 1:
    print(list('1'))
else:
    print('Not a nonnegative integer')


        