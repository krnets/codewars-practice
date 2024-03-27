from kata import testit
import codewars_test as test

@test.describe("True or False")
def true_or_false():
    
    @test.it("Example Tests")
    def example_tests():
        # n ?
        test.assert_equals(testit(0), 0)
        test.assert_equals(testit(0), 0)
        # n - 1 ?
        test.assert_equals(testit(2), 1)
        test.assert_equals(testit(3), 2)
        # round(n / 3.0)
        test.assert_equals(testit(4), 1)
        test.assert_equals(testit(5), 2)
        test.assert_equals(testit(6), 2)
        # None of the above
        test.assert_equals(testit(7), 3)
        test.assert_equals(testit(8), 1)
        test.assert_equals(testit(9), 2)
        test.assert_equals(testit(10), 2)
        test.assert_equals(testit(100), 3)
        test.assert_equals(testit(1000), 6)
        test.assert_equals(testit(10000), 5)