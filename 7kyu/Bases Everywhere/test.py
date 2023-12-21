import codewars_test as test
from kata import base_finder

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(base_finder(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']), 10)
        test.assert_equals(base_finder(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']), 10)
        test.assert_equals(base_finder(['1', '2', '3', '4', '5', '6', '10', '11', '12', '13']), 7)
        test.assert_equals(base_finder(['301', '302', '303', '304', '305', '310', '311', '312', '313', '314']), 6)
        test.assert_equals(base_finder(['50', '51', '61', '53', '54', '60', '52', '62', '55', '56']), 7)