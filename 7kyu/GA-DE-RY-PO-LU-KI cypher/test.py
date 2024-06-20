import codewars_test as test
from kata import encode, decode

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(encode("ABCD") , "GBCE", "Expected 'GBCE'")
        test.assert_equals(encode("GBCE") , "ABCD", "Expected 'ABCD'")
        test.assert_equals(encode("Gug hgs g cgt") , "Ala has a cat", "Expected 'Ala has a cat'")
        test.assert_equals(decode("agedyropulik") , "gaderypoluki", "Expected 'gaderypoluki'")
        test.assert_equals(decode("Ala has a cat") , "Gug hgs g cgt", "Expected 'Gug hgs g cgt'")
        test.assert_equals(decode("gaderypoluki") , "agedyropulik", "Expected 'agedyropulik'")