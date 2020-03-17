# 7kyu - Simple string reversal II

""" In this Kata, you will be given a string and two indexes. 
Your task is to reverse the portion of that string between those two indices inclusive.

solve("codewars",1,5) = "cawedors" -- elements at index 1 to 5 inclusive are "odewa". So we reverse them.
solve("cODEWArs", 1,5) = "cAWEDOrs" -- to help visualize.

Input will be lowercase and uppercase letters only.  """

def solve(st, a, b):
    return st[0:a] + st[a:b+1][::-1] + st[b+1:]


q = solve("codewars", 1, 5)  # "cawedors"
q
q = solve("codingIsFun", 2, 100)  # "conuFsIgnid"
q
q = solve("FunctionalProgramming", 2, 15)  # "FuargorPlanoitcnmming"
q
q = solve("abcefghijklmnopqrstuvwxyz", 0, 20)  # "vutsrqponmlkjihgfecbawxyz"
q
q = solve("abcefghijklmnopqrstuvwxyz", 5, 20)  # "abcefvutsrqponmlkjihgwxyz"
q
