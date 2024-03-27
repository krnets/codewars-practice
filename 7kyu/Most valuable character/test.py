import codewars_test as test
from kata import solve

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_tests():        
        test.assert_equals(solve('a'), 'a')
        test.assert_equals(solve('aa'), 'a')
        test.assert_equals(solve('bcd'), 'b')
        test.assert_equals(solve('axyzxyz'), 'x') 
        test.assert_equals(solve('aabccc'), 'c') 