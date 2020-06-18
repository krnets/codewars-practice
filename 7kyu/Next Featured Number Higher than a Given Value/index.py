""" 7kyu - Next Featured Number Higher than a Given Value

Make a function that receives a value, val and outputs the smallest higher number than the given value, 
and this number belong to a set of positive integers that have the following properties:

    their digits occur only once
    they are odd
    they are multiple of three

next_numb(12) == 15
next_numb(13) == 15
next_numb(99) == 105
next_numb(999999) == 1023459
next_number(9999999999) == "There is no possible number that fulfills those requirements" """


# def next_numb(val):
#     while val < 1e9:
#         val += 1
#         if val % 2 and val % 3 == 0 and len(set(str(val))) == len(str(val)):
#             return val
#     return "There is no possible number that fulfills those requirements"

# def next_numb(val):
#     val += 1
#     while val % 3:
#         val += 1
#     if val % 2 == 0:
#         val += 3
#     while len(set(str(val))) != len(str(val)):
#         if val > 1e9:
#             return "There is no possible number that fulfills those requirements"
#         val += 6
#     return val

def valid(s):
    return len(set(s)) == len(s)


def next_numb(val):
    val += 3 - val % 3
    val += 3 if not val & 1 else 0

    while not valid(str(val)):
        if val > 1e9:
            return "There is no possible number that fulfills those requirements"
        val += 6

    return val


q = next_numb(12), 15
q
q = next_numb(13), 15
q
q = next_numb(99), 105
q
q = next_numb(999999), 1023459
q
q = next_numb(
    9999999999), "There is no possible number that fulfills those requirements"
q
