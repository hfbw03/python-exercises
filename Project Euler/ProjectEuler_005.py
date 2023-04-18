# ProjectEuler_005

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def lcm_array(arr):
    # Initialize lcm as the first element in array
    lcm = arr[0]

    # Iteration through the rest of the array to calculate GCD using the Euclidean algorithm.
    for i in range(1, len(arr)):

        # Setting num1 to lcm and num2 to the current integer being considered.
        num1 = lcm
        num2 = arr[i]
        gcd = 1

        # The algorithm repeatedly takes the modulus of num1 and num2 and swaps them until num2 = 0.
        # When num2 = 0, num1 contains the GCD of the two numbers.
        while num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp

        # Once the GCD is found, the function calculates the LCM.
        # LCM is the product of the two numbers divided by their GCD.
        gcd = num1
        lcm = (lcm * arr[i]) // gcd

    return lcm

arr1 = list(range(1,21))
print(lcm_array(arr1))

# the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is 232792560.