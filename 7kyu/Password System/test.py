import codewars_test as test
from kata import help_zoom

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(help_zoom([1, 1, 0, 0, 0, 0, 0, 1, 1 ]) , "Yes")
        test.assert_equals(help_zoom([1, 1, 0, 0, 0, 0, 1, 1, 0 ]) , "No")
        test.assert_equals(help_zoom([1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1 ]) , "Yes")    
        test.assert_equals(help_zoom([1, 0, 1, 1, 0, 0, 0, 0, 0 ]) , "No")
        test.assert_equals(help_zoom([1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1 ]) , "No")
