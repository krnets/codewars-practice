# Beta - Sum of all arguments

""" Calculate the sum of all the arguments passed to a function.

Note: If any of the arguments is not a finite number the function should return False 
instead of the sum of the arguments.

sum(1,2,3,4)         should return 10
sum(1, "two", 3)     should return false
sum(1, 2, [3], NaN)  should return false """


def sum_all(*args):
    return all(isinstance(x, int) for x in args) and sum(args)


q = sum_all(6, 2, 3)  # 11
q
q = sum_all(756, 2, 1, 10)  # 769
q
q = sum_all(76856, -32, 1981, 1076)  # 79881
q
q = sum_all(1, -32, "codewars", 1076)  # False
q
q = sum_all(7, -3452, 1981, 1076)  # -388
q
