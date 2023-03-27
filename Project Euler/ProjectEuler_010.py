# ProjectEuler_010

# Start Date : 2/25/2023
# Solved Date: 2/28/2023

'''  
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

# (Copied base code, will go through code later)

# To find the sum of prime numbers in python from 2 to n.

# Defining the function 
def Sum_Of_Primes(n):
# creating a list to store the prime numbers
	prime = [True] * (n + 1)
	
# We have created a boolean array "prime[0..n]".
# We initialize all the entries as true.
# Logic: The value in prime[i] is if it's prime it will be True, else False. 
	
	s = 2
# As the prime numbers start from 2.
	while s * s <= n:
# If the prime[s] is not changing, then it is a prime hence TRUE.
		if prime[s] == True:
# We update all the multiples of s if the prime is TRUE. This is how the sieve of Eratosthenes works.
			i = s * 2
			while i <= n:
				prime[i] = False
				i += s
		s = s + 1
		
# We return the sum of primes generated through the Sieve of Eratosthenes.
	sum = 0
	for i in range (2, n + 1):
		if (prime[i]):
			sum = sum + i
	return sum

n = int(input("\nPlease enter the last number up to which the sum of prime number is to be found:"))
print("\nThe sum of prime numbers in python from 1 to" , n, "is:",Sum_Of_Primes(n))

# The sum of prime numbers in python from 1 to 2000000 is 142913828922.