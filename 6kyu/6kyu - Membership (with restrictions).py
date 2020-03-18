# 6kyu - Membership (with restrictions)

""" Determine the client's membership level based on the invested amount of money and the given thresholds for membership levels.

There are four membership levels (from highest to lowest): 
Platinum, Gold, Silver, Bronze

The minimum investment is the threshold limit for Bronze membership. 
If the given amount is less than the Bronze treshold limit return Not a member.

A client belongs to a membership level when his invested amount is greater than or equal the level's threshold amount.

|--------+----------+------+--------+--------+--------------+------------------|
| Amount | Platinum | Gold | Silver | Bronze | Result       | Explanations     |
|--------+----------+------+--------+--------+--------------+------------------|
|   7000 |    10000 | 8000 |   6000 |   4000 | Silver       | Amount >= Silver |
|   3000 |    10000 | 8000 |   6000 |   5000 | Not a member | Amount < Bronze  |
|   8000 |    12000 | 8000 |   7000 |   5000 | Gold         | Amount >= Gold   |
|--------+----------+------+--------+--------+--------------+------------------|

Restrictions

    The first line of your code has to be def membership(amount, platinum, gold, silver, bronze):
    Your code except for the firt line mustn't contain the words platinum, gold, silver, bronze 
    or they reversed forms (e.g. dlog) or any string which contains these words or they reversed forms. 
    (The check is case-insensitive.)
    Must not contain: +, %, {, }.

Disclaimer

This kata is about creativity not proper coding style. """


def membership(amount, platinum, gold, silver, bronze):
    ordered = reversed(sorted((v, k) for k, v in locals().items() if k != 'amount'))
    return next((level.capitalize() for threshold, level in ordered if amount >= threshold), 'Not a member')


q = membership(100000, 1000000, 100000, 10000, 1000)  # "Gold"
q
q = membership(1001, 1000000, 100000, 10000, 1000)  # "Bronze"
q
q = membership(998, 1000000, 100000, 10000, 1000)  # "Not a member"
q
q = membership(0, 1000000, 100000, 10000, 1000)  # "Not a member"
q
