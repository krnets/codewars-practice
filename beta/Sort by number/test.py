import codewars_test as test
from kata import sort_by_num

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sort_by_num('b9i5a8f3d7h4e6c2g1'), 'g1c2f3h4i5e6d7a8b9')
        test.assert_equals(sort_by_num('a3h9c4i1d2e7f8g6b5' ), 'i1d2a3c4b5g6e7f8h9')