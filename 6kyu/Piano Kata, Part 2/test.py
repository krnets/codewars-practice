import codewars_test as test
from kata import which_note

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(which_note(1), "A")
        test.assert_equals(which_note(5), "C#")
        test.assert_equals(which_note(12), "G#")
        test.assert_equals(which_note(42), "D")
        test.assert_equals(which_note(88), "C")
        test.assert_equals(which_note(89), "A")
        test.assert_equals(which_note(92), "C")
        test.assert_equals(which_note(100), "G#")
        test.assert_equals(which_note(111), "G")
        test.assert_equals(which_note(200), "G#")
        test.assert_equals(which_note(2017), "F")