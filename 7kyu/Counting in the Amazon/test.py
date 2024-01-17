import codewars_test as test
from kata import count_arara


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(count_arara(1), "anane")
        test.assert_equals(count_arara(2), "adak")
        test.assert_equals(count_arara(3), "adak anane")
        test.assert_equals(count_arara(9), "adak adak adak adak anane")
