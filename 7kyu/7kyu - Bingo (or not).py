# 7kyu - Bingo ( Or Not )

""" For this game of BINGO, you will receive a single array of 10 numbers from 1 to 26 as an input. 
Duplicate numbers within the array are possible.

Each number corresponds to their alphabetical order letter (e.g. 1 = A. 2 = B, etc). 
Write a function where you will win the game if your numbers can spell "BINGO". 
They do not need to be in the right order in the input array). Otherwise you will lose. 
Your outputs should be "WIN" or "LOSE" respectively. """


# def bingo(array):
#     chars = [chr(x + 64) for x in array]
#     return 'WIN' if len([c for c in 'BINGO' if c in chars]) == len('BINGO') else 'LOSE'

BINGO = {ord(c)-64 for c in 'BINGO'}

# def bingo(array):
#     return 'LOSE' if len(BINGO.difference(array)) else 'WIN'

def bingo(array):
    return 'WIN' if set(array) >= BINGO else 'LOSE'


q = bingo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "LOSE"
q
q = bingo([20, 12, 23, 14, 6, 22, 12, 17, 2, 26]), "LOSE"
q
q = bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]), "WIN"
q
q = bingo([5, 2, 13, 7, 5, 14, 17, 15, 9, 10]), "WIN"
q
