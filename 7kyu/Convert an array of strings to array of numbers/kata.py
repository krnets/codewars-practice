def to_float_array(arr):
    return [*map(float, arr)]


q = to_float_array(["1.1", "2.2", "3.3"])  # [1.1, 2.2, 3.3]
q
q = to_float_array(["1", "2", "3"])  # [1, 2, 3]
q
