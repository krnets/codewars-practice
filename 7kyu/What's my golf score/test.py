import codewars_test as test
from kata import golf_score_calculator

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(golf_score_calculator('443454444344544443', '353445334534445344'), -1);