import codewars_test as test
from kata import no_ifs_no_buts


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(no_ifs_no_buts(45, 51), "45 is smaller than 51")
        test.assert_equals(no_ifs_no_buts(1, 2), "1 is smaller than 2")
        test.assert_equals(no_ifs_no_buts(-3, 2), "-3 is smaller than 2")
        test.assert_equals(no_ifs_no_buts(1, 1), "1 is equal to 1")
        test.assert_equals(no_ifs_no_buts(100, 100), "100 is equal to 100")
        test.assert_equals(no_ifs_no_buts(100, 80), "100 is greater than 80")
        test.assert_equals(no_ifs_no_buts(20, 19), "20 is greater than 19")
