import codewars_test as test
from kata import calculate


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(calculate("Panda has 48 apples and loses 4"), 44)
        test.assert_equals(calculate("Jerry has 34 apples and gains 6"), 40)
        test.assert_equals(calculate("Tom has 20 apples and gains 15"), 35)
        test.assert_equals(calculate("Fred has 110 bananas and loses 50"), 60)
        test.assert_equals(calculate("Pippi has 20 tunas and gains 0"), 20)
