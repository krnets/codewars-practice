import codewars_test as test
from kata import two_highest


@test.describe("Fixed tests")
def fixed_tests():
    @test.it("Tests")
    def it_1():
        test.assert_equals(two_highest([]), [])
        test.assert_equals(two_highest([15]), [15])
        test.assert_equals(two_highest([1, 1, 1]), [1])
        test.assert_equals(two_highest([4, 10, 10, 9]), [10, 9])
        test.assert_equals(two_highest([15, 20, 20, 17]), [20, 17])


@test.describe("Random tests")
def random_tests():
    import random
    import heapq

    @test.it("Tests")
    def it_1():
        for i in range(200):
            a = random.sample(range(100000), random.randint(1, 50))
            result = heapq.nlargest(2, sorted(a))
            test.assert_equals(two_highest(a), result)
