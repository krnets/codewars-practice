from collections import Counter, defaultdict
import codewars_test as test


# def delete_nth(order, max_e):
#     freq = Counter(order)
#     for k, v in freq.items():
#         if v > max_e:
#             freq[k] = max_e
#     res = []
#     for x in order:
#         if freq[x] > 0:
#             res.append(x)
#             freq[x] -= 1
#     return res


def delete_nth(order, max_e):
    freq = defaultdict(int)
    res = []
    for x in order:
        freq[x] += 1
        if freq[x] <= max_e:
            res.append(x)
    return res


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            delete_nth([20, 37, 20, 21], 1),
            [20, 37, 21],
            "From list [20, 37, 20, 21], 1 you get",
        )
        test.assert_equals(
            delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3),
            [1, 1, 3, 3, 7, 2, 2, 2],
            "From list [1, 1, 3, 3, 7, 2, 2, 2, 2], 3 you get",
        )
        test.assert_equals(
            delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3),
            [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5],
            "From list [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3 you get",
        )
        test.assert_equals(
            delete_nth([1, 1, 1, 1, 1], 5),
            [1, 1, 1, 1, 1],
            "From list [1, 1, 1, 1, 1], 5 you get",
        )
        test.assert_equals(delete_nth([], 5), [], "From list [], 5 you get")
        test.assert_equals(
            delete_nth([12, 39, 19, 39, 39, 19, 12], 1),
            [12, 39, 19],
            "From list [12, 39, 19, 39, 39, 19, 12], 1 you get",
        )
