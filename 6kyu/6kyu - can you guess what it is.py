# 6kyu - can you guess what it is ?

""" You've just entered a programming contest and have a chance to win a million dollars. 
This is the last question you have to solve, so your victory (and your vacation) depend on it. 
Can you guess the function just by looking at the test cases? 
There are two numerical inputs and one numerical output. Goodluck! """


TABLE = str.maketrans('0123456789', '9876543210')

def code(x, y):
    return sum(int(str(n).translate(TABLE)) for n in [x, y])

# def code(x, y):
#     return sum(int('9' * len(str(n))) - n for n in [x, y])

q = code(9, 8), 1
q
q = code(123, 456), 1419
q
q = code(3, 2), 13
q
q = code(1, 1), 16
q
q = code(12, 8), 88
q
q = code(200, 100), 1698
q
q = code(100, 200), 1698
q
