import codewars_test as test
from kata import repeat_sequence_len

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(repeat_sequence_len(1), 1)
        test.assert_equals(repeat_sequence_len(85), 8)
        test.assert_equals(repeat_sequence_len(810), 8)
        test.assert_equals(repeat_sequence_len(812), 8)
        test.assert_equals(repeat_sequence_len(818), 1)
        test.assert_equals(repeat_sequence_len(833), 1)