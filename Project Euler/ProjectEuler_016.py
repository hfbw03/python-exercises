# ProjectEuler_016

'''
2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ** 1000?
'''

# Convert 2 ** 1000 to str.
bigpower = str(2 ** 1000)

# Initializing the sum of the digits to 0.
digits_sum = 0

# Iterate through the digits and add them all.
for i in bigpower:
        digits_sum += int(i)

print(digits_sum)
    
# The sum of the digits of the number 2 ** 1000 is 1366.
# This problem can actually be solved with one line of code but this is what I came up with.