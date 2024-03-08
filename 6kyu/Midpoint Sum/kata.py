def midpoint_sum(ints):
    right_sum = sum(ints)
    left_sum = 0
    
    if len(ints) > 2 and right_sum > 1:
        for i, x in enumerate(ints):
            right_sum -= x
            if left_sum == right_sum:
                return i
            left_sum += x
