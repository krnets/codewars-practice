import codewars_test as test
from kata import divisible_by_last

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(divisible_by_last(73312), [False, False, True, False, True])
        test.assert_equals(divisible_by_last(2026), [False, True, False, True])
        test.assert_equals(divisible_by_last(635), [False, False, False])
        test.assert_equals(divisible_by_last(1337), [False, True, True, False])
