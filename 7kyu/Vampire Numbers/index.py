# 7kyu - Vampire Numbers

""" Our loose definition of Vampire Numbers can be described as follows:

6 * 21 = 126
# 6 and 21 would be valid 'fangs' for a vampire number as the 
# digits 6, 1, and 2 are present in both the product and multiplicands

10 * 11 = 110
# 110 is not a vampire number since there are three 1's in the
# multiplicands, but only two 1's in the product

Create a function that can receive two 'fangs' and determine if the product of the two is a valid vampire number. """

# def vampire_test(x, y):
#     return ''.join(sorted(str(x) + str(y))) == ''.join(sorted(str(x * y)))

# def vampire_test(x, y):
#     return sorted(str(x) + str(y)) == sorted(str(x * y))

def vampire_test(x, y):
    return sorted(str(x * y)) == sorted(str(x) + str(y))

q = vampire_test(21,6) # True, "Basic: 21 * 6 = 126 should return True"
q
q = vampire_test(204,615) # True, "Basic: 204 * 615 = 125460 should return True"
q
q = vampire_test(30,-51) # True, "One Negative: 30 * -51 = -1530 should return True"
q
q = vampire_test(-246,-510) # False, "Double Negatives: -246 * -510 = 125460 should return False (The negative signs aren't present on the product)"
q
q = vampire_test(210,600) # True, "Trailing Zeroes: 210 * 600 = 126000 should return True"
q
