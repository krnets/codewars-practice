import codewars_test as test
from kata import number_format

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(number_format(100000), "100,000")
        test.assert_equals(number_format(5678545), "5,678,545")
        test.assert_equals(number_format(-420902), "-420,902")
        test.assert_equals(number_format(-3), "-3")
        test.assert_equals(number_format(-1003), "-1,003")