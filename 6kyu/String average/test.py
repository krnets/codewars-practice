import codewars_test as test
from kata import average_string

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(average_string("zero nine five two"), "four")
        test.assert_equals(average_string("four six two three"), "three")
        test.assert_equals(average_string("one two three four five"), "three")
        test.assert_equals(average_string("five four"), "four")
        test.assert_equals(average_string("zero zero zero zero zero"), "zero")
        test.assert_equals(average_string("one one eight one"), "two")
        test.assert_equals(average_string("one"), "one")
        test.assert_equals(average_string(""), "n/a")
        test.assert_equals(average_string("ten"), "n/a")
        test.assert_equals(average_string("pippi"), "n/a")