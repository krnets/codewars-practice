import codewars_test as test
from kata import get_num

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(get_num(300), 2, "Wrong output!")
        test.assert_equals(get_num(90783), 4, "Wrong output!")
        test.assert_equals(get_num(123321), 0, "Wrong output!")
        test.assert_equals(get_num(89282350306), 8, "Wrong output!")
        test.assert_equals(get_num(3479283469), 5, "Wrong output!")