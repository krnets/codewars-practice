import codewars_test as test
from kata import get_score

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(get_score(1), 50, 'get_score(1) returns a wrong result')
        test.assert_equals(get_score(2), 150, 'get_score(2) returns a wrong result')
        test.assert_equals(get_score(3), 300, 'get_score(3) returns a wrong result')
        test.assert_equals(get_score(4), 500, 'get_score(4) returns a wrong result')
        test.assert_equals(get_score(5), 750, 'get_score(5) returns a wrong result')