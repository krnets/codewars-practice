import codewars_test as test
from kata import determine_time


@test.describe("Fixed tests")
def fixed_tests():
    @test.it("Tests")
    def it_1():
        test.assert_equals(determine_time(["01:00:00", "02:30:00"]), True)
        test.assert_equals(determine_time(["01:00:00", "02:30:00", "22:00:00"]), False)
        test.assert_equals(determine_time(["12:00:00", "12:00:00"]), True)
        test.assert_equals(determine_time([]), True)
