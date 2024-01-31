import codewars_test as test
from kata import count_smileys

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(count_smileys([]), 0)
        test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
        test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
        test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)