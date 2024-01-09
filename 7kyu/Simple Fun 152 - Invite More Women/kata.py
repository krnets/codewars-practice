def invite_more_women(arr):
    return sum(arr) > 0


q = invite_more_women([1, -1, 1])  # True
q
q = invite_more_women([-1, -1, -1])  # False
q
q = invite_more_women([1, -1])  # False
q
q = invite_more_women([1, 1, 1])  # True
q
