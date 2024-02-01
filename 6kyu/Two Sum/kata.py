def two_sum(numbers, target):
    number_index_dict = {}
    for i, x in enumerate(numbers):
        complement = target - x
        if complement in number_index_dict:
            return (i, number_index_dict[complement])
        number_index_dict[x] = i
