import codewars_test as test


# def max_sequence(arr):
#     running_sum, min_val, ans = 0, 0, 0
#     for x in arr:
#         running_sum += x
#         min_val = min(min_val, running_sum)
#         ans = max(ans, running_sum - min_val)
#     return ans


# def max_sequence(arr):
#     ans, running_sum = 0, 0
#     for x in arr:
#         running_sum += x
#         if running_sum < 0:
#             running_sum = 0
#         if running_sum > ans:
#             ans = running_sum
#     return ans


# def max_sequence(arr):
#     ans, running_sum = 0, 0
#     for x in arr:
#         running_sum += x
#         running_sum = max(0, running_sum)
#         ans = max(ans, running_sum)
#     return ans


def max_sequence(arr):
    ans, running_max = 0, 0
    for x in arr:
        running_max = max(0, x + running_max)
        ans = max(ans, running_max)
    return ans


@test.describe("Fixed tests")
def tests():

    @test.it("Should work on an empty array")
    def test_empty_array():
        test.assert_equals(max_sequence([]), 0)

    @test.it(
        "Should obtain correct maximum subarray sum in the array from the kata description example"
    )
    def test_example_array():
        test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    @test.it(
        "Should obtain correct maximum subarray sum in an example with negative numbers"
    )
    def test_negative_array():
        test.assert_equals(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)

    @test.it("Should obtain correct maximum subarray sum in a complex example")
    def test_complex_array():
        test.assert_equals(
            max_sequence(
                [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]
            ),
            155,
        )
