# 8kyu - Transportation on vacation

""" After a hard quarter in the office you decide to get some rest on a vacation. 
So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. 
The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. 
Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d). """

# def rental_car_cost(d):
#     if d < 3:
#         return 40 * d
#     elif d >= 3 and d < 7:
#         return 40 * d - 20
#     else:
#         return 40 * d - 50

def rental_car_cost(d):
    discount = 0
    if d >= 7:
        discount = 50
    elif d >= 3:
        discount = 20
    return d * 40 - discount

# def rental_car_cost(d):
#     discount = 50 if d >= 7 else 20 if d >= 3 else 0
#     return d * 40 - discount

# def rental_car_cost(d):
#     total = d * 40
#     if d >= 7:
#         total -= 50
#     elif d >= 3:
#         total -= 20
#     return total


q = rental_car_cost(1)  # 40
q
q = rental_car_cost(4)  # 140
q
q = rental_car_cost(7)  # 230
q
q = rental_car_cost(8)  # 270
q
