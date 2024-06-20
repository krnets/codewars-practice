def get_length_of_missing_array(array_of_arrays):
    lengths = array_of_arrays and all(array_of_arrays) and [*map(len, array_of_arrays)]
    return bool(lengths) and sum(range(min(lengths), max(lengths) + 1)) - sum(lengths)
