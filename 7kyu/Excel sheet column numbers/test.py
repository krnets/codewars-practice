import codewars_test as test
from kata import title_to_number

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(title_to_number('A'),1)
        test.assert_equals(title_to_number('Z'),26)
        test.assert_equals(title_to_number('AA'),27)
        test.assert_equals(title_to_number('AZ'),52)
        test.assert_equals(title_to_number('BA'),53)
        test.assert_equals(title_to_number('CODEWARS'),28779382963)
        test.assert_equals(title_to_number('ZZZTOP'),321268054)
        test.assert_equals(title_to_number('OYAJI'),7294985)
        test.assert_equals(title_to_number('LONELINESS'),68400586976949)
        test.assert_equals(title_to_number('UNFORGIVABLE'),79089429845931757)