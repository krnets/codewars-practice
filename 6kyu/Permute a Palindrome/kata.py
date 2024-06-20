from collections import Counter

def permute_a_palindrome(input):
    v = Counter(input).values()
    return all(i % 2 == 0 for i in v) or sum(i & 1 for i in v) == 1