import codewars_test as test
from kata import work_needed

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(work_needed(60, [(1,0)]), "Easy Money!")
        test.assert_equals(work_needed(60, [(0,0)]), "I need to work 1 hour(s) and 0 minute(s)")
        test.assert_equals(work_needed(141, [(1,55), (0,25)]), "I need to work 0 hour(s) and 1 minute(s)")