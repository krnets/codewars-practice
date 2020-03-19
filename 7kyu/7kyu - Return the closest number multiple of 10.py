# 7kyu - Return the closest number multiple of 10

""" Given a number return the closest number to it that is divisible by 10.

22  ->  20
25  ->  30
37  ->  40  """


# def closest_multiple_10(i):
#     return round(i / 10) * 10

def closest_multiple_10(i):
    return round(i, -1)


q = closest_multiple_10(54)  # 50
q
q = closest_multiple_10(55)  # 60
q
