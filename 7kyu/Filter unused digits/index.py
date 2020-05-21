# 7kyu - Filter unused digits

""" Given few numbers, you need to print out the digits that are not being used.

Example:

unused_digits(12, 34, 56, 78) # "09"
unused_digits(2015, 8, 26) # "3479"

Note:

    Result string should be sorted
    The test case won't pass Integer with leading zero """


# def unused_digits(*args):
#     cmp = ''.join(map(str, list(args)))
#     res = list(filter(lambda x: str(x) not in cmp, list(range(10))))
#     return ''.join(map(str, res))

# def unused_digits(*args):
#     cmp = ''.join(map(str, list(args)))
# return ''.join(str(x) for x in range(10) if str(x) not in cmp)

def unused_digits(*args):
    return ''.join(n for n in '0123456789' if n not in str(args))

# def unused_digits(*args):
#     return ''.join(str(x) for x in range(10) if str(x) not in str(args))

# def unused_digits(*ints):
#     return ''.join(sorted(list(set('0123456789') - set(c for i in ints for c in str(i)))))

# def unused_digits(*args):
#     return ''.join(sorted(set('0123456789') - set(str(args))))


q = unused_digits(12, 34, 56, 78)  # "09"
q
q = unused_digits(2015, 8, 26)  # "3479"
q
q = unused_digits(276, 575)  # "013489"
q
q = unused_digits(643)  # "0125789"
q
q = unused_digits(864, 896, 744)  # "01235"
q
