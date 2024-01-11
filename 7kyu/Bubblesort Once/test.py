import codewars_test as test
from kata import bubblesort_once


@test.describe("bubblesort_once")
def test_suite():
    @test.it("should work for an example test")
    def example_assertion():
        test.assert_equals(
            bubblesort_once([9, 7, 5, 3, 1, 2, 4, 6, 8]), [7, 5, 3, 1, 2, 4, 6, 8, 9]
        )

    @test.it("should work for some fixed tests")
    def fixed_assertions():
        test.assert_equals(bubblesort_once([1, 2]), [1, 2])
        test.assert_equals(bubblesort_once([2, 1]), [1, 2])
        test.assert_equals(bubblesort_once([1, 3]), [1, 3])
        test.assert_equals(bubblesort_once([3, 1]), [1, 3])
        test.assert_equals(bubblesort_once([24, 57]), [24, 57])
        test.assert_equals(bubblesort_once([89, 36]), [36, 89])
        test.assert_equals(bubblesort_once([1, 2, 3]), [1, 2, 3])
        test.assert_equals(bubblesort_once([2, 4, 1]), [2, 1, 4])
        test.assert_equals(bubblesort_once([17, 5, 11]), [5, 11, 17])
        test.assert_equals(bubblesort_once([25, 16, 9]), [16, 9, 25])
        test.assert_equals(bubblesort_once([103, 87, 113]), [87, 103, 113])
        test.assert_equals(bubblesort_once([1032, 3192, 2864]), [1032, 2864, 3192])
        test.assert_equals(bubblesort_once([1, 2, 3, 4]), [1, 2, 3, 4])
        test.assert_equals(bubblesort_once([2, 3, 4, 1]), [2, 3, 1, 4])
        test.assert_equals(bubblesort_once([3, 4, 1, 2]), [3, 1, 2, 4])
        test.assert_equals(bubblesort_once([4, 1, 2, 3]), [1, 2, 3, 4])
        test.assert_equals(bubblesort_once([7, 5, 3, 1]), [5, 3, 1, 7])
        test.assert_equals(bubblesort_once([5, 3, 7, 7]), [3, 5, 7, 7])
        test.assert_equals(bubblesort_once([3, 1, 8, 5]), [1, 3, 5, 8])
        test.assert_equals(bubblesort_once([1, 9, 5, 5]), [1, 5, 5, 9])
        test.assert_equals(
            bubblesort_once([6, 3, 4, 9, 1, 2, 7, 8, 5]), [3, 4, 6, 1, 2, 7, 8, 5, 9]
        )
        test.assert_equals(
            bubblesort_once([6, 3, 4, 15, 14, 9, 1, 2, 7, 8, 5, 14, 11, 15, 17, 19]),
            [3, 4, 6, 14, 9, 1, 2, 7, 8, 5, 14, 11, 15, 15, 17, 19],
        )

    @test.it("should work for some edge cases")
    def edge_assertions():
        test.assert_equals(
            bubblesort_once([42]),
            [42],
            "Your function should work for lists containing exactly 1 integer",
        )
        test.assert_equals(
            bubblesort_once([]), [], "Your function should work for empty lists"
        )

    @test.it("should be pure, i.e. not mutate the original list")
    def purity_assertions():
        l = [2, 5, 3, 7, 1, 10, 4, 6, 8, 9]
        result = bubblesort_once(l)
        test.assert_equals(
            result,
            [2, 3, 5, 1, 7, 4, 6, 8, 9, 10],
            "Your function should produce the correct results",
        )
        test.expect(
            l is not result,
            "Your function should return a new list not the original list",
        )
        test.assert_equals(
            l,
            [2, 5, 3, 7, 1, 10, 4, 6, 8, 9],
            "Your function should not mutate the original list",
        )

    @test.it("should work for random tests")
    def random_assertions():
        from random import randint

        def solution(l):
            l = [n for n in l]
            i = 0
            while i < len(l) - 1:
                if l[i] > l[i + 1]:
                    tmp = l[i]
                    l[i] = l[i + 1]
                    l[i + 1] = tmp
                i += 1
            return l

        for _ in range(100):
            l = []
            size = randint(10, 99)
            for _ in range(size):
                l.append(randint(0, 999))
            expected = solution(l)
            actual = bubblesort_once(l)
            test.assert_equals(actual, expected)
