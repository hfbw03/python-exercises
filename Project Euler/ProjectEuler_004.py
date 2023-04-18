# ProjectEuler_004

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 
2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def largestPalindrome(n):
    # Special case for 1-digit numbers (largest palindrome for two 1-digit numbers is 9).
    if n == 1:
        return 9
    
    # Define the minimum number for n digits. (ex: for n = 3, min_num = 100)
    min_num = 10 ** (n - 1)

    # Define the maximum number for n digits. (ex: for n = 3, max_num = 999)
    max_num = 10 ** n - 1

    # Variable to keep track of the largest palindrome found so far.
    largestPal = 0

    # The outer loop iterates over all odd numbers between max_num and min_num - 1)
    # The -2 in the range function is to ensure that the loop only iterates over odd numbers.
    for i in range(max_num, min_num - 1, -2):
        if i * i < largestPal:
            break

        # Same idea for inner loop
        for j in range(max_num, i - 1, -2):
            product = i * j

            # A palindrome with an even number of digits must be divisible by 11.
            # Also checks if the product is larger or equal to the current largest palindrome.
            if product % 11 != 0 and product >= largestPal:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                continue

            # This line checks if the product is a palindrome. It converts the product into a string,
            # and compares it to the reverse of the string using the [::-1] slicing syntax.
            if str(product) == str(product)[::-1]:
                largestPal = product

    return largestPal

print(largestPalindrome(3))

# The largest palindrome made from the product of two 3-digit numbers is 906609.