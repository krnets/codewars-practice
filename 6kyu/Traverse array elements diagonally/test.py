import random
import codewars_test as test
from kata import diagonal


@test.describe("My Fixed Tests")
def my_tests():
    @test.it("My Test Cases")
    def basic_test_cases():
        # test.assert_equals( diagonal([[1, 6, 7], [7, 2, 4], [3, 5, 9]]), [[9], [4, 5], [7, 2, 3], [6, 7], [1]], "Oops! Wrong",)
        test.assert_equals(
            diagonal([[1, 6, 7], [7, 2, 4], [3, 5, 9]]),
            [9, 4, 5, 7, 2, 3, 6, 7, 1],
            "Oops! Wrong",
        )


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(diagonal([[7]]), [7], "Oops! Wrong")
        test.assert_equals(
            diagonal([[4, 5, 7], [3, 9, 1], [7, 6, 2]]),
            [2, 1, 6, 7, 9, 7, 5, 3, 4],
            "Oops! Wrong",
        )


@test.describe("Random Tests")
def random_tests():
    def diagonal_76yu(ar):
        cols, rows, res = len(ar[0]), len(ar), []
        for n in range(0, cols + rows):
            r, c, arr = n, 0, []
            while r >= 0 and c < cols:
                if r < rows:
                    arr.append(ar[r][c])
                r -= 1
                c += 1
            res.append(arr)
        t = [i for j in res for i in j]
        t.reverse()
        return t

    def nxn(n):
        arr, i = [], 0
        while i < n:
            temp, j = [], 0
            while j < n:
                temp.append(random.randrange(0, 15))
                j += 1
            arr.append(temp)
            i += 1
        return arr

    for i in range(0, 200):
        n = random.randrange(1, 10)
        nbn = nxn(n)
        expected = diagonal_76yu(nbn[:])

        @test.it(f"ar = {nbn[:]}")
        def basic_test_cases():
            test.assert_equals(diagonal(nbn[:]), expected, "Oops! Wrong")
