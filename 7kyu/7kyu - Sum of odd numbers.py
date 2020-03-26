# 7kyu - Sum of odd numbers

""" Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8 """


def row_sum_odd_numbers(n):
    return n ** 3


q = row_sum_odd_numbers(1)  # 1
q
q = row_sum_odd_numbers(2)  # 8
q
q = row_sum_odd_numbers(3)  # 27
q
q = row_sum_odd_numbers(4)  # 64
q
q = row_sum_odd_numbers(13)  # 2197
q
q = row_sum_odd_numbers(19)  # 6859
q
q = row_sum_odd_numbers(41)  # 68921
q
