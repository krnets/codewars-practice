# 8kyu - Convert number to reversed array of digits

""" Given a random number:

    C#: long;
    C++: unsigned long;

You have to return the digits of this number within an array in reverse order.

348597 => [7,9,5,8,4,3] """


# def digitize(n):
#     return [int(x) for x in list(reversed(str(n)))]

# def digitize(n):
#     return [int(x) for x in reversed(str(n))]

# def digitize(n):
#     return [int(x) for x in str(n)][::-1]

def digitize(n):
    return list(map(int, str(n)))[::-1]

# def digitize(n):
#     return list(map(int, reversed(str(n))))

q = digitize(35231)  # [1,3,2,5,3]
q
