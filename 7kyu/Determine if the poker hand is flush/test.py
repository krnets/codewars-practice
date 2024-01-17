import codewars_test as test
from kata import is_flush


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(is_flush(["AS", "3S", "9S", "KS", "4S"]), True)
        test.assert_equals(is_flush(["AD", "4S", "7H", "KC", "5S"]), False)
        test.assert_equals(is_flush(["AD", "4S", "10H", "KC", "5S"]), False)
        test.assert_equals(is_flush(["QD", "4D", "10D", "KD", "5D"]), True)
