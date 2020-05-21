# 7kyu - The Coins of Ter | Round to the Next N

""" Write a function adjust, that takes a two integers: 
the lowest currency unit that's still allowed, and the price/debt that needs to get adjusted. 
All prices are going up, and debts are remitted. 
The lowest currency will always be positive.

In other words: adjust takes two integers, b and n, and returns the smallest number k, 
such that n <= k and k % b == 0. """


def adjust(coin, price):
    return price + (coin - price) % coin


q = adjust(3, 0)  # 0
q
q = adjust(3, 1)  # 3
q
q = adjust(3, -2)  # 0
q
q = adjust(3, -4)  # -3
q
q = adjust(3, 3)  # 3
q
q = adjust(3, 6)  # 6
q
q = adjust(3, 7)  # 9
q
