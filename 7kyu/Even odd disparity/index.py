# 7kyu - Even odd disparity

""" Given an array, return the difference between the count of even numbers and the count of odd numbers. 
0 will be considered an even number.

For example:

solve([0,1,2,3]) = 0 because there are two even numbers and two odd numbers. 
Even - Odd = 2 - 2 = 0.  

Let's now add two letters to the last example:

solve([0,1,2,3,'a','b']) = 0. 
Again, Even - Odd = 2 - 2 = 0. Ignore letters. 

The input will be an array of lowercase letters and numbers only.

Haskell: 
solve ["0","1","2","3","a","b"] = 0 -- In Haskell, all array elements will be strings.

Other languages: 
solve([0, 1 ,2, 3, 'a', 'b']) = 0 """


# def solve(a):
#     even = [x for x in a if isinstance(x, int) and x % 2 == 0]
#     odd  = [x for x in a if isinstance(x, int) and x % 2 != 0]
#     return len(even) - len(odd)

# def solve(a):
#     return sum(isinstance(x, int) and [1, -1][x % 2] for x in a)

def solve(a):
    return sum([1, -1][x % 2] for x in a if isinstance(x, int))


q = solve([0, 1, 2, 3])  # 0
q
q = solve([0, 1, 2, 3, 'a', 'b'])  # 0
q
q = solve([0, 15, 'z', 16, 'm', 13, 14, 'c', 9, 10, 13, 'u', 4, 3])  # 0
q
q = solve([13, 6, 8, 15, 4, 8, 13])  # 1
q
q = solve([1, 'a', 17, 8, 'e', 3, 'i', 12, 1])  # -2
q
