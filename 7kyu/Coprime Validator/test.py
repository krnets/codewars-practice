import codewars_test as test
from kata import are_coprime


@test.describe("Coprime Validator")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(are_coprime(20, 27), True, "The numbers were 20 and 27")
        test.assert_equals(are_coprime(12, 39), False, "The numbers were 12 and 39")
