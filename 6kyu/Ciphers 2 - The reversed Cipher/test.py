import codewars_test as test
from kata import encode

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(encode("Hello World!"),"lleHo dlroW!")