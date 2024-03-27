import codewars_test as test
from kata import make_parts

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(make_parts([1,2,3,4,5], 2), [[1,2],[3,4],[5]])
        test.assert_equals(make_parts([1,2,3], 1), [[1],[2],[3]])
        test.assert_equals(make_parts([1,2,3,4,5], 10), [[1,2,3,4,5]])