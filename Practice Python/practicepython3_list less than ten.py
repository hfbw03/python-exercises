# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 22:31:30 2022

@author: Lenovo
"""

someList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

print('Enter a number below:')
number = int(input( ))

for x in someList:
    if x < number:
        newList.append(x)
        newList.sort()
print(newList)
