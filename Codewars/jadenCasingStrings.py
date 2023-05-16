# Jaden Casing Strings
# https://www.codewars.com/kata/5390bac347d09b7da40006f6

def to_jaden_case(string):
    words = string.split()
    capital_words = []
    for i in words:
        capital_words.append(i.capitalize())
    jaden_cased_string = " ".join(capital_words)
    return jaden_cased_string

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

# Simpler solution:
'''
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
'''