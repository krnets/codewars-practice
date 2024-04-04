import codewars_test as test
from kata import shortest_steps_to_num

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(shortest_steps_to_num(1), 0)
        test.assert_equals(shortest_steps_to_num(12), 4)
        test.assert_equals(shortest_steps_to_num(16), 4)
        test.assert_equals(shortest_steps_to_num(71), 9)