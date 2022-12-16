from itertools import count
from math import ceil


# def movie(card, ticket, perc):
#     n_visits = 0
#     system_A = 0
#     system_B = card
#     curr_ticket_price = ticket

#     while system_A <= ceil(system_B):
#         system_A += ticket
#         curr_ticket_price *= perc
#         system_B += curr_ticket_price
#         n_visits += 1

#     return n_visits


# def movie(card, ticket, perc):
#     return next(n for n in count(1)
#                 if ceil(card + ticket * perc * (1 - perc ** n) / (1 - perc)) < ticket * n)

# def movie(card, ticket, perc):
#     return next(n for n in count(card // ticket)
#                 if ceil(card + ticket * perc * (1 - perc ** n) / (1 - perc)) < ticket * n)


# def movie(card, ticket, perc):
#     for n in count(card // ticket):
#         system_A = ticket * n
#         system_B = ceil(card + ticket * perc * (1 - perc**n) / (1 - perc))

#         if system_B < system_A:
#             return n

def movie(card_balance, ticket_price, discount_perc):
    for n in count(card_balance // ticket_price):
        system_A = ticket_price * n
        system_B = ceil(card_balance + ticket_price * discount_perc * (1 - discount_perc**n) / (1 - discount_perc))

        if system_B < system_A:
            return n


q = movie(500, 15, 0.9)  # 43
q
q = movie(100, 10, 0.95)  # 24
q
