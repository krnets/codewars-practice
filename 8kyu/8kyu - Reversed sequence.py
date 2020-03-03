# 8kyu - Reversed sequence

""" Get the number n (n>0) to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1] """


# def reverse_seq(n):
#     return list(range(1, n + 1))[::-1]

def reverse_seq(n):
    return list(range(n, 0, -1))


q = reverse_seq(5)  # [5,4,3,2,1]
q
