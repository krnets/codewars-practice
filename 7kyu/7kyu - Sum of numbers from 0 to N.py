# 7kyu - Sum of numbers from 0 to N

""" We want to generate a function that computes the series 
starting from 0 and ending until the given number.

6
0+1+2+3+4+5+6 = 21

-15
-15<0

0
0=0 """


def show_sequence(n):
    if n > 0:
        seq = range(n+1)
        return '+'.join(str(x) for x in seq) + ' = ' + str(sum(seq))
    elif n == 0:
        return '0=0'
    else:
        return str(n) + '<0'


q = show_sequence(6)  # "0+1+2+3+4+5+6 = 21"
q
q = show_sequence(7)  # "0+1+2+3+4+5+6+7 = 28"
q
q = show_sequence(0)  # "0=0"
q
q = show_sequence(-1)  # "-1<0"
q
q = show_sequence(-10)  # "-10<0"
q
