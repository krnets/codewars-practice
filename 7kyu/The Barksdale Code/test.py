import codewars_test as test
from kata import decode

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(decode("4103432323"), "6957678787")
        test.assert_equals(decode("4103438970"), "6957672135")
        test.assert_equals(decode("4104305768"), "6956750342")
        test.assert_equals(decode("4102204351"), "6958856709")
        test.assert_equals(decode("4107056043"), "6953504567")