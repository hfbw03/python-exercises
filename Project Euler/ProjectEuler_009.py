# ProjectEuler_008

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a ** 2 + b ** 2 = c ** 2

For example, 3 ** 2 + 4 ** 2 = 25 = 5 ** 2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
'''

# Defining a function to find a pythagorean triplet that equal a specific number n.
def pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a + 1, n):
            c = n - a - b
            if c > 0 and a * a + b * b == c * c:
                print(a * b * c)
                return (a, b, c)
    return None
            
print(pythagorean_triplet(1000))

# The pythagorean triplet is (200, 375, 425) and the product is 31875000.
