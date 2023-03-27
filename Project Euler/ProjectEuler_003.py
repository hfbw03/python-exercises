# ProjectEuler_003

# Start Date : 2/24/2023
# Solved Date: 2/25/2023

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Since the prime is a big number, brute force is not an option.

# Answer is copied directly straight from a website, hence I only consider this as done after I finish understanding
# how the code works and explaining it. Also, I probably need to get better at placing comments in my code.

def largest_prime_factor(n):
    # We start with 2 because it's the smallest possible factor.  
    i = 2  
    # The smallest prime factor of a composite number N is less than or equal to √N. We can use this fact to optimize our code.
    # Also, in factor trees, the last iteration will always be two of the same number.
    while i * i <= n:  
        # If n has a remainder after division by i, i equals i + 1.
        if n % i:  
            i += 1
        # If n has no remainder, n equals n floor-divided by i. This line gives us i * n. 
        else:  
            n //= i  
    # Eventually the program will end at either n or i * n, and the last iteration's n is our largest prime factor.
    return n  
      
print(largest_prime_factor(600851475143))  

# The largest prime factor of 600851475143 is 6857.

# Worth noting that this code is more easily understood by visualizing it as a factor tree.