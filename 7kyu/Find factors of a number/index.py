# 7kyu - Find factors of a number

""" Create a function that takes a number and finds the factors of it, listing them in descending order in an array.

If the parameter is not an integer or less than 1, return -1.

Example: factors(54) should return [54, 27, 18, 9, 6, 3, 2, 1] """


# def factors(x):
#     if not isinstance(x, int) or x < 1:
#         return -1
#     return [num for num in range(x, 0, -1) if x % num == 0]

def factors(x):
    return [i for i in range(x, 0, -1) if x % i == 0] if isinstance(x, int) and x > 0 else -1


# returns -1 for numbers less than or equal to zero
q = factors(-4), -1
q
q = factors(0), -1
q
q = factors(-12), -1
q

# returns -1 for non-integers
q = factors('a'), -1
q
q = factors(4.5), -1
q
q = factors('hello world'), -1
q

# returns the correct answer for some examples
q = factors(54), [54, 27, 18, 9, 6, 3, 2, 1]
q
q = factors(49), [49, 7, 1]
q
q = factors(1), [1]
q
