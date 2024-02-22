import codewars_test as test
from kata import min_value_array

test.it("Basic Tests")

arr1 = [[1, 2, 3, 4], [-1, 0, 4, 3], [0, 6, 7, -2]]
test.assert_equals(list(min_value_array(arr1)), [-1, 0, 3, -2])

arr2 = [[0, 0, 0, 0, 0], [1, 2, 3, 4, 5], [3, 4, 5, 6, 7]]
test.assert_equals(list(min_value_array(arr2)), [0, 0, 0, 0, 0])

arr3 = [[1, 2, 3, 4, 5]]
test.assert_equals(list(min_value_array(arr3)), [1, 2, 3, 4, 5])
