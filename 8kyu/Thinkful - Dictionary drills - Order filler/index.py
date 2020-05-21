# 8kyu - Thinkful - Dictionary drills: Order filler

""" You're running an online business and a big part of your day is fulfilling orders. 
As your volume picks up that's been taking more of your time, and unfortunately lately 
you've been running into situations where you take an order but can't fulfill it.

You've decided to write a function fillable() that takes three arguments: 

a dictionary stock representing all the merchandise you have in stock, 
a string merch representing the thing your customer wants to buy, 
and an integer n representing the number of units of merch they would like to buy. 

Your function should return True if you have the merchandise in stock to complete the sale, otherwise it should return False.

Valid data will always be passed in and n will always be >= 1. """

stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5,
}


# def fillable(stock, merch, n):
#     return stock[merch] >= n if merch in stock else False

# def fillable(stock, merch, n):
#     return merch in stock and stock[merch] >= n

def fillable(stock, merch, n):
    return stock.get(merch, 0) >= n


q = fillable(stock, 'football', 3)  # True
q
q = fillable(stock, 'leggos', 2)  # False
q
q = fillable(stock, 'action figure', 1)  # False
q
