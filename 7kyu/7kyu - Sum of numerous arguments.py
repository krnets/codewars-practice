# 7kyu - Sum of numerous arguments

""" After calling the function findSum() with any number of non-negative integer arguments, 
it should return the sum of all those arguments. If no arguments are given, the function 
should return 0, if negative arguments are given, it should return -1.


find_sum(1,2,3,4); # returns 10 
find_sum(1,-2);    # returns -1 
find_sum();        # returns 0 

Hint: research the arguments object on google or read Chapter 4 from Eloquent Javascript """


def find_sum(*args):
    return -1 if any(x < 0 for x in args) else sum(args)


q = find_sum(1, 3, 5)  # 9, "1 + 3 + 5 = 9"
q
q = find_sum()  # 0, "If no arguments, function should return 0"
q
# -1, "If negative arguments are passed, function should return -1"
q = find_sum(1, -2, 4)
q
q = find_sum(0)  # 0, "The sum of 0 is 0"
q
q = find_sum(1, 1, 5)  # 7, "Your sum is incorrect"
q
q = find_sum(1, 1, 1, 1, 1, 1, 1, 1, 0)  # 8, "Your sum is incorrect"
q
q = find_sum(-1, -1, 5)  # -1, "Your sum is incorrect"
q
q = find_sum(-1, -1, -5)  # -1, "Your sum is incorrect"
q
q = find_sum(0, -1, 5)  # -1, "Your sum is incorrect"
q
q = find_sum(0, 0, 0)  # 0, "Your sum is incorrect"
q
