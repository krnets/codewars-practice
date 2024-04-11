import codewars_test as test
from kata import mirror

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(mirror("Hello World"), "*********\n* olleH *\n* dlroW *\n*********");
        test.assert_equals(mirror("Codewars"), "************\n* srawedoC *\n************"); 
        test.assert_equals(mirror("emosewA !ataK"), "***********\n* Awesome *\n* Kata!   *\n***********");
