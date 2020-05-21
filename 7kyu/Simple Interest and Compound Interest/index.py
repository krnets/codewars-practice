# 7kyu - Simple Interest and Compound Interest

""" Simple interest on a loan is calculated by simply taking the initial amount (the principal, p) 
and multiplying it by a rate of interest (r) and the number of time periods (n).

Compound interest is calculated by adding the interest after each time period to the amount owed, 
then calculating the next interest payment based on the principal PLUS the interest from all previous periods.

Given a principal p, interest rate r, and a number of periods n, return an array 
[total owed under simple interest, total owed under compound interest].

EXAMPLES:

interest(100,0.1,1) = [110,110]
interest(100,0.1,2) = [120,121]
interest(100,0.1,10) = [200,259]

Round all answers to the nearest integer. Principal will always be an integer between 0 and 9999; 
interest rate will be a decimal between 0 and 1; number of time periods will be an integer between 0 and 49.  """

# def interest(p, r, n):
#     simple = p * (1 + r * n)
#     compound = p
#     for i in range(1, n+1):
#         compound += compound * r
#     return list(map(round, [simple, compound]))

# def interest(p, r, n):
#     simple = p * (1 + (r * n))
#     compound = p * (1 + r) ** n
#     return list(map(round, [simple, compound]))

def interest(p, r, n):
    simple = p * (1 + (r * n))
    compound = p * pow(1 + r,  n)
    return list(map(round, [simple, compound]))


q = interest(100, 0.1, 1), [110, 110]
q
q = interest(100, 0.1, 2), [120, 121]
q
q = interest(100, 0.1, 10), [200, 259]
q
