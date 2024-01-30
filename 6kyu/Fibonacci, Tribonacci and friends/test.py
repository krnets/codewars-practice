import codewars_test as test
from kata import xbonacci as xbonacci
    

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(xbonacci([1,2,3,4,5,6,7,8,9,0],0),[])
        test.assert_equals(xbonacci([0,1],10),[0,1,1,2,3,5,8,13,21,34])
        test.assert_equals(xbonacci([1,1],10),[1,1,2,3,5,8,13,21,34,55])
        test.assert_equals(xbonacci([0,0,0,0,1],10),[0,0,0,0,1,1,2,4,8,16])
        test.assert_equals(xbonacci([1,0,0,0,0,0,1],10),[1,0,0,0,0,0,1,2,3,6])
        test.assert_equals(xbonacci([1,0,0,0,0,0,0,0,0,0],20),[1,0,0,0,0,0,0,0,0,0,1,1,2,4,8,16,32,64,128,256])
        test.assert_equals(xbonacci([0.5,0,0,0,0,0,0,0,0,0],10),[0.5,0,0,0,0,0,0,0,0,0])
        test.assert_equals(xbonacci([0.5,0,0,0,0,0,0,0,0,0],20),[0.5,0,0,0,0,0,0,0,0,0,0.5,0.5,1,2,4,8,16,32,64,128])
        test.assert_equals(xbonacci([0,0,0,0,0,0,0,0,0,0],20),[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        test.assert_equals(xbonacci([1,2,3,4,5,6,7,8,9,0],9),[1,2,3,4,5,6,7,8,9])