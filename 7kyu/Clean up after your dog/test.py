import codewars_test as test
from kata import crap

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(crap([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 2, 2), "Clean")
        test.assert_equals(crap([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 1, 1), "Cr@p")
        test.assert_equals(crap([['_','_'], ['_','@'], ['D','_']], 2, 2), "Dog!!")
        test.assert_equals(crap([['_','_','_','_'], ['_','_','_','_'], ['_','_','_', '_']], 2, 2), "Clean")
        test.assert_equals(crap([['@','@'], ['@','@'], ['@','@']], 3, 2), "Clean")