import codewars_test as test
from kata import is_pronic

@test.describe("Figurate Numbers #2 - Pronic Number")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(is_pronic(0),True,'0 is a Pronic Number');
        test.assert_equals(is_pronic(1),False,'1 is not a Pronic Number')
        test.assert_equals(is_pronic(2),True,'2 is a Pronic Number')
        test.assert_equals(is_pronic(3),False,'3 is not a Pronic Number')
        test.assert_equals(is_pronic(4),False,'4 is not a Pronic Number')
        test.assert_equals(is_pronic(5),False,'5 is not a Pronic Number')
        test.assert_equals(is_pronic(6),True,'6 is a Pronic Number')
        test.assert_equals(is_pronic(-3),False,'-3 is not a Pronic Number')
        test.assert_equals(is_pronic(-27),False,'-27 is not a Pronic Number')