# 7kyu - Maximum Product

""" Given an array of integers, find the maximum product obtained from multiplying 2 adjacent numbers in the array.

    Array/list size is at least 2.
    Array/list numbers could be a mixture of positives, negatives also zeroes .

Input >> Output Examples

adjacentElementsProduct([1, 2, 3]); ==> return 6
    The maximum product obtained from multiplying 2 * 3 = 6, and they're adjacent numbers in the array.

adjacentElementsProduct([9, 5, 10, 2, 24, -1, -48]); ==> return 50
    Max product obtained from multiplying 5 * 10 = 50.

adjacentElementsProduct([-23, 4, -5, 99, -27, 329, -2, 7, -921])  ==>  return -14
    The maximum product obtained from multiplying -2 * 7 = -14, and they're adjacent numbers in the array. """


# def adjacent_element_product(array):
#     res = []
#     for i in range(len(array) - 1):
#         res.append(array[i] * array[i + 1])
#     return max(res)

# def adjacent_element_product(array):
#     return max(array[i] * array[i+1] for i in range(len(array)-1))

def adjacent_element_product(array):
    return max(x * y for x, y in zip(array, array[1:]))


# Test.it("Positive numbers")
q = adjacent_element_product([5, 8])  # 40
q
q = adjacent_element_product([1, 2, 3])  # 6
q
q = adjacent_element_product([1, 5, 10, 9])  # 90
q
q = adjacent_element_product([4, 12, 3, 1, 5])  # 48
q
q = adjacent_element_product([5, 1, 2, 3, 1, 4])  # 6
q

# Test.it("Both positive and negative values")
q = adjacent_element_product([3, 6, -2, -5, 7, 3])  # 21
q
q = adjacent_element_product([9, 5, 10, 2, 24, -1, -48])  # 50
q
q = adjacent_element_product([5, 6, -4, 2, 3, 2, -23])  # 30
q
q = adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921])  # -14
q
q = adjacent_element_product([5, 1, 2, 3, 1, 4])  # 6
q

# Test.it("Contains zeroes")
q = adjacent_element_product([1, 0, 1, 0, 1000])  # 0
q
q = adjacent_element_product([1, 2, 3, 0])  # 6
q
