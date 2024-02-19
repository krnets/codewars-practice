from kata import swap_adjacent_bits
import codewars_test as test

@test.describe("Sample tests")
def sample_tests():
    @test.it("should work for basic tests")
    def _():
        test.assert_equals(swap_adjacent_bits(13), 14, "For n = 13")
        test.assert_equals(swap_adjacent_bits(74), 133, "For n = 74")
        test.assert_equals(swap_adjacent_bits(1073741823), 1073741823, "For n = 1073741823")
        test.assert_equals(swap_adjacent_bits(0), 0, "For n = 0")
        test.assert_equals(swap_adjacent_bits(1), 2, "For n = 1")
        test.assert_equals(swap_adjacent_bits(83748), 166680, "For n = 83748")