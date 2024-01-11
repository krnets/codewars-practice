import codewars_test as test
from kata import next_happy_year

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(next_happy_year(1001),1023)
        test.assert_equals(next_happy_year(1123),1203)
        test.assert_equals(next_happy_year(2001),2013)
        test.assert_equals(next_happy_year(2334),2340)
        test.assert_equals(next_happy_year(3331),3401)
        test.assert_equals(next_happy_year(1987),2013)
        test.assert_equals(next_happy_year(5555),5601)
        test.assert_equals(next_happy_year(7712),7801)
        test.assert_equals(next_happy_year(8088),8091)
        test.assert_equals(next_happy_year(8999),9012)
