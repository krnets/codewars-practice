""" 7kyu - Sort by Example

Given an Array and an Example-Array to sort to, write a function that sorts the Array following the Example-Array.

Assume Example Array catalogs all elements possibly seen in the input Array. 
However, the input Array does not necessarily have to have all elements seen in the Example.

Example:

Arr: [1,3,4,4,4,4,5]

Example Arr: [4,1,2,3,5]

Result: [4,4,4,4,1,3,5] """


# def example_sort(arr, example_arr):
#     example_dict = {v: i for i, v in enumerate(example_arr)}
#     return sorted(arr, key=lambda x: example_dict[x])

# def example_sort(arr, example_arr):  # not as efficient as dict.get
#     return sorted(arr, key=example_arr.index)

def example_sort(arr, example_arr):
    example_dict = {x: i for i, x in enumerate(example_arr)}
    return sorted(arr, key=example_dict.get)

# def example_sort(arr, example_arr):
#     return [a for e in example_arr for a in arr if a == e]


q = example_sort([1, 2, 3, 4, 5], [2, 3, 4, 1, 5])
q
#      [2,3,4,1,5]
q = example_sort([1, 2, 3, 3, 3, 4, 5], [2, 3, 4, 1, 5])
q
#      [2,3,3,3,4,1,5]
q = example_sort([1, 2, 3, 3, 3, 5], [2, 3, 4, 1, 5])
q
#      [2,3,3,3,1,5]
q = example_sort([1, 2, 3, 3, 3, 5], [3, 4, 5, 6,
                                      9, 11, 12, 13, 1, 7, 8, 2, 10])
q
#      [3,3,3,5,1,2]
q = example_sort(["a", "a", "b", "f", "d", "a"],
                 ["c", "a", "d", "b", "e", "f"])
q
#      ["a","a","a","d","b","f"]
q = example_sort(["Alice", "Bryan", "Chad", "Darrell", "Ellie", "Fiona"], [
                 "Alice", "Bryan", "Chad", "Darrell", "Ellie", "Fiona"])
q
#      ["Alice","Bryan","Chad","Darrell","Ellie","Fiona"])
