import codewars_test as test
from kata import beggars

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(beggars([1,2,3,4,5],1),[15])
        test.assert_equals(beggars([1,2,3,4,5],2),[9,6])
        test.assert_equals(beggars([1,2,3,4,5],3),[5,7,3])
        test.assert_equals(beggars([1,2,3,4,5],6),[1,2,3,4,5,0])
        test.assert_equals(beggars([1,2,3,4,5],0),[])