# 7kyu - Sum of odd numbers

""" Given the triangle of consecutive odd numbers:

                      1                            = 1
                   3     5                         = 8
                7     9    11                      = 27
            13    15    17    19                   = 64
         21    23    25    27    29                = 125
      31    33    35    37    39    41             = 216
   43    45    47    49    51    53    55          = 343
57    59    61    63    65    67    69    71       = 512
...

Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8 """


# def row_sum_odd_numbers(n):
#     return n ** 3

# def row_sum_odd_numbers(n):
#     return sum(range(n*(n-1)+1, n*(n+1), 2))

# def row_sum_odd_numbers(n):
#     return n * n * n

def row_sum_odd_numbers(n):
    # return (n*(n-1)+1, n*(n+1)-1)
    # return [*range(n*(n-1)+1, n*(n+1), 2)]
    return sum([*range(n*(n-1)+1, n*(n+1), 2)])

q = row_sum_odd_numbers(1)  # 1
q
q = row_sum_odd_numbers(2)  # 8
q
q = row_sum_odd_numbers(3)  # 27
q
q = row_sum_odd_numbers(4)  # 64
q
q = row_sum_odd_numbers(5)  # 125
q
q = row_sum_odd_numbers(6)  # 216
q
q = row_sum_odd_numbers(7)  # 343
q
q = row_sum_odd_numbers(8)  # 512
q
q = row_sum_odd_numbers(13)  # 2197
q
q = row_sum_odd_numbers(16)  # 4096
q
q = row_sum_odd_numbers(19)  # 6859
q
q = row_sum_odd_numbers(32)  # 32768
q
q = row_sum_odd_numbers(41)  # 68921
q
