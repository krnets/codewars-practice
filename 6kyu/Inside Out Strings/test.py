import codewars_test as test
from kata import inside_out

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(inside_out('man i need a taxi up to ubud'), 'man i ende a atix up to budu')
        test.assert_equals(inside_out('what time are we climbing up the volcano'), 'hwta item are we milcgnib up the lovcona')
        test.assert_equals(inside_out('take me to semynak'), 'atek me to mesykan')