import codewars_test as test
from kata import combine

@test.describe("Fixed Tests")
def fixed_tests():
    objA = { 'a': 10, 'b': 20, 'c': 30 }
    objB = { 'a': 3, 'c': 6, 'd': 3 }
    objC = { 'a': 5, 'd': 11, 'e': 8 }
    objD = { 'c': 3 }
    
    @test.it('Combine 2 objects')
    def basic_test_cases():
        test.assert_equals(combine(objA, objB), { 'a': 13, 'b': 20, 'c': 36, 'd': 3 })
        test.assert_equals(combine(objA, objC), { 'a': 15, 'b': 20, 'c': 30, 'd': 11, 'e': 8 })
    
    @test.it('Combine 3 objects')
    def basic_test_cases():
        test.assert_equals(combine(objA, objB, objC), { 'a': 18, 'b': 20, 'c': 36, 'd': 14, 'e': 8 })
        test.assert_equals(combine(objA, objC, objD), { 'a': 15, 'b': 20, 'c': 33, 'd': 11, 'e': 8 })
    
    @test.it('Handle empty objects')
    def basic_test_cases():
        test.assert_equals(combine({}, {}, {}), {})
        test.assert_equals(combine(objA, objC, {}), { 'a': 15, 'b': 20, 'c': 30, 'd': 11, 'e': 8 })

    @test.it('more edge tests')
    def basic_test_cases():
        test.assert_equals(combine({}), {})
        test.assert_equals(combine(objA, objA, objA), { 'a': 30, 'b': 60, 'c': 90})
        test.assert_equals(combine(objD, objD, objD, objD, objD, objD), { 'c': 18})
        test.assert_equals(combine(objA, {}, objA), { 'a': 20, 'b': 40, 'c': 60})