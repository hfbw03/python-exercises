# ProjectEuler_007

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
'''

primes = []

def SieveOfErathosthenes():
    n = 10000000
    prime = [True] * (n + 1)
    # Creating a boolean array and initializing all the values as True.

    p = 2
    while (p*p <= n):
        if prime[p] == True:
            for i in range(p*p, n+1, p):
                prime[i] = False
                # Multiples of primes are marked False.
        p += 1
        # The process repeats with the next number.
    
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
            # Prime numbers are appended to the primes list

SieveOfErathosthenes()
print(primes[10000])

# The 10,001st prime number is 104743.