import codewars_test as test
from kata import count_red_beads


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(count_red_beads(1), 0)
        test.assert_equals(count_red_beads(3), 4)
        test.assert_equals(count_red_beads(5), 8)
