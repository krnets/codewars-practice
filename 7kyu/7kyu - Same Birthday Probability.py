# 7kyu - Same Birthday Probability

""" Given n number of people in a room, calculate the probability that any two people in that room 
have the same birthday (assume 365 days every year = ignore leap year). 
Answers should be two decimals unless whole (0 or 1) eg 0.05 """


# def calculate_probability(n):
#     acc = 1
#     for i in range(1, n):
#         acc *= 1 - i/365
#     return round(1-acc, 2)

# def calculate_probability(n, p=1):
#     for i in range(n):
#         p *= 365 - i
#     return round(1 - p / 365**n, 2)

def calculate_probability(n, p=1):
    for i in range(n):
        p *= 365 - i
    return round(1 - p/365**n, 2)


q = calculate_probability(5), 0.03
q
q = calculate_probability(15), 0.25
q
q = calculate_probability(19), 0.38
q
q = calculate_probability(39), 0.88
q
q = calculate_probability(1), 0
q
q = calculate_probability(365), 1
q
q = calculate_probability(366), 1
q
