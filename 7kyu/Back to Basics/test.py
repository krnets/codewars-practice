import codewars_test as test
from kata import types

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Simple Cases')
    def example_cases():
        test.assert_equals(types(10), "int")
        test.assert_equals(types(9.7), "float")
        test.assert_equals(types("Hello"), "str")
        test.assert_equals(types(True), "bool")