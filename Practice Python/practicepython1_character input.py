# Practice Python Exercise 1
# Character Input
# Simple program that asks the user's name and age and returns the year when they'll turn 100.
# This program doesn't take into account the date and month of birth.

print('Hello, stranger.')

print('Please input your name.')
name = input()

print('Please input your age.')
age = int(input())

print('You will be 100 years old in ' + str((2022 + 100 - age)) + '.')    
