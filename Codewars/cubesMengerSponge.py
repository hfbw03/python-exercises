# Count cubes in a Menger Sponge
# https://www.codewars.com/kata/59d28768a25c8c51a6000057

def calc_ms(n):
    if n >= 0:
        return(20 ** n)
    else:
        print("Please input a nonnegative integer.")

print(calc_ms(3))