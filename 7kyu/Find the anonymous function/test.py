import codewars_test as test
from kata import find_function

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_function([lambda a: a%2==0,9,3,1,0],[1,2,3,4]), [2,4])
        test.assert_equals(find_function([9,3,lambda a: a%2,1,0],[1,2,3,4]), [1,3])
        test.assert_equals(find_function([9,3,lambda a: a%13==0,1,0],[1,2,3,4]), [])
        test.assert_equals(find_function([9,3,lambda a: a%13!=0,1,0],[1,2,3,4]), [1,2,3,4])
        test.assert_equals(find_function([5,'a',lambda a: a*4!=0,1,0],[0,1,2,3,4]), [1,2,3,4])