from random import randrange as ran
import codewars_test as test
from kata import solve

@test.describe('Fixed Tests')
def fixed_tests():

    @test.it('Basic Test Cases')
    def basic_tests():
        test.assert_equals(solve(0,10),3)
        test.assert_equals(solve(10,100),4)
        test.assert_equals(solve(100,1000),12)
        test.assert_equals(solve(1000,10000),20)
        test.assert_equals(solve(10000,15000),6)
        test.assert_equals(solve(15000,20000),9)
        test.assert_equals(solve(60000,70000),15)
        test.assert_equals(solve(60000,130000),55)