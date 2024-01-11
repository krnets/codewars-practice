import codewars_test as test
from kata import cake

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(cake(900, 'abcdef'), 'That was close!')
        test.assert_equals(cake(56, 'ifkhchlhfd'), 'Fire!')
        test.assert_equals(cake(256, 'aaaaaddddr'), 'Fire!')
        test.assert_equals(cake(333, 'jfmgklfhglbe'), 'Fire!')
        test.assert_equals(cake(12, 'jaam'), 'Fire!')
        test.assert_equals(cake(339, 'aoq'), 'Fire!')