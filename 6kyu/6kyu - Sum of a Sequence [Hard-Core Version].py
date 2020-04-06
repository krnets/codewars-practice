# 6kyu - Sum of a Sequence [Hard-Core Version]

""" The task is simple to explain: simply sum all the numbers from the first parameter 
being the beginning to the second parameter being the upper limit (possibly included), 
going in steps expressed by the third parameter:

sequence_sum(2, 2, 2) # 2
sequence_sum(2, 6, 2) # 12 (= 2 + 4 + 6)
sequence_sum(1, 5, 1) # (= 1 + 2 + 3 + 4 + 5)
sequence_sum(1, 5, 3) # 5 (= 1 + 4)

If it is an impossible sequence (with the beginning being larger the end and a positive step 
or the other way around), just return 0.

Note: differing from the other base kata, much larger ranges are going to be tested, 
so you should hope to get your algo optimized and to avoid brute-forcing your way through the solution. """

def sequence_sum(begin, end, step):
    n = (end - begin) // step
    return 0 if n < 0 else (n + 1) * (n * step + 2 * begin) // 2


q = sequence_sum(2, 6, 2)  # 12
q
q = sequence_sum(1, 5, 1)  # 15
q
q = sequence_sum(1, 5, 3)  # 5
q
q = sequence_sum(-1, -5, -3)  # -5
q
q = sequence_sum(16, 15, 3)  # 0
q
q = sequence_sum(-24, -2, 22)  # -26
q
q = sequence_sum(-2, 4, 658)  # -2
q
q = sequence_sum(780, 6851543, 5)  # 4694363402480
q
q = sequence_sum(9383, 71418, 2)  # 1253127200
q
q = sequence_sum(20, 673388797, 5)  # 45345247259849570
q
