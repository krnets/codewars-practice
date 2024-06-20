import codewars_test as test
from kata import sortme

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sortme(["Hello", "there", "I'm", "fine"]), ["fine", "Hello", "I'm", "there"])
        test.assert_equals(sortme(["C", "d", "a", "B"]), ["a", "B", "C", "d"])
        test.assert_equals(sortme(["CodeWars"]), ["CodeWars"])
        test.assert_equals(sortme([]), [])