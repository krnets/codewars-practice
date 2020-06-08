# 7kyu - Graceful Tipping

""" Adding tip to a restaurant bill in a graceful way can be tricky, thats why you need make a function for it.

The function will receive the restaurant bill (always a positive number) as an argument. 
You need to 1) add at least 15% in tip, 2) round that number up to an elegant value and 3) return it.

What is an elegant number? It depends on the magnitude of the number to be rounded. 
Numbers below 10 should simply be rounded to whole numbers. 
Numbers 10 and above should be rounded like this:

10 - 99.99... ---> Round to number divisible by 5
100 - 999.99... ---> Round to number divisible by 50
1000 - 9999.99... ---> Round to number divisible by 500

 1  -->    2
 7  -->    9
12  -->   15
86  -->  100 """

import math


def graceful_tipping(bill):
    bill *= 1.15
    dec = int(10 ** len(str(int(bill))) / 20) if bill > 10 else 1
    return math.ceil(bill / dec) * dec


q = graceful_tipping(1), 2
q
q = graceful_tipping(7), 9
q

q = graceful_tipping(12), 15
q
q = graceful_tipping(86), 100
q

q = graceful_tipping(99), 150
q

q = graceful_tipping(1149), 1500
q
q = graceful_tipping(983212), 1500000
q
