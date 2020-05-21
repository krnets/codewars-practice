# 7kyu - String to list of integers

""" Given a string containing a list of integers separated by commas, write the function string_to_int_list(s) 
that takes said string and returns a new list containing all integers present in the string, preserving the order.

For example, give the string "-1,2,3,4,5", the function string_to_int_list() should return [-1,2,3,4,5]

Please note that there can be one or more consecutive commas whithout numbers, like so: "-1,-2,,,,,,3,4,5,,6" """


# def string_to_int_list(s):
#     return [int(x) for x in s.replace(',', ' ').split()]

def string_to_int_list(s):
    return [int(x) for x in s.split(',') if x]


q = string_to_int_list("1,2,3,4,5")
q
#      [1, 2, 3, 4, 5]

q = string_to_int_list("-2,-1,3,4,5")
q
#      [-2, -1, 3, 4, 5]

q = string_to_int_list("21,12,23,34,45")
q
#      [21, 12, 23, 34, 45]
