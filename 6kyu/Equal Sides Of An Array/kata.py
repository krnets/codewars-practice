<<<<<<< HEAD
<<<<<<< HEAD
import codewars_test as test


def find_even_index(arr):
    right_sum = sum(arr)
    left_sum = 0

    for i, x in enumerate(arr):
        right_sum -= x
        if left_sum == right_sum:
            return i
        left_sum += x

    return -1


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(find_even_index([1, 2, 3, 4, 3, 2, 1]), 3)
        test.assert_equals(
            find_even_index([1, 100, 50, -51, 1, 1]),
            1,
        )
        test.assert_equals(find_even_index([1, 2, 3, 4, 5, 6]), -1)
        test.assert_equals(find_even_index([20, 10, 30, 10, 10, 15, 35]), 3)
        test.assert_equals(find_even_index([20, 10, -80, 10, 10, 15, 35]), 0)
        test.assert_equals(find_even_index([10, -80, 10, 10, 15, 35, 20]), 6)
        test.assert_equals(find_even_index(list(range(1, 100))), -1)
        test.assert_equals(
            find_even_index([0, 0, 0, 0, 0]),
            0,
            "Should pick the first index if more cases are valid",
        )
        test.assert_equals(find_even_index([-1, -2, -3, -4, -3, -2, -1]), 3)
        test.assert_equals(find_even_index(list(range(-100, -1))), -1)
        test.assert_equals(find_even_index([8, 8]), -1)
        test.assert_equals(find_even_index([8, 0]), 0)
        test.assert_equals(find_even_index([0, 8]), 1)
        test.assert_equals(find_even_index([7, 3, -3]), 0)
        test.assert_equals(find_even_index([8]), 0)
        test.assert_equals(find_even_index([10, -10]), -1)
        test.assert_equals(find_even_index([-3, 2, 1, 0]), 3)
        test.assert_equals(
            find_even_index(
                [-15, 5, 11, 17, 19, -17, 20, -6, 17, -17, 19, 16, -15, -6, 20, 17]
            ),
            8,
        )
=======
=======
>>>>>>> 677620fbe53501cdc7d184005fe8b1a8b16722c1
def find_even_index(arr):
    sum_right = sum(arr)
    sum_left = 0

    for i, x in enumerate(arr):
        sum_right -= x
        if sum_left == sum_right:
            return i
        sum_left += x

    return -1
<<<<<<< HEAD
>>>>>>> 677620fbe53501cdc7d184005fe8b1a8b16722c1
=======
>>>>>>> 677620fbe53501cdc7d184005fe8b1a8b16722c1
