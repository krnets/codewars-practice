import codewars_test as test
from kata import is_valid

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('should return true for valid identifiers')
    def example_cases():
        test.assert_equals(is_valid("okay_ok1"), True, "Wrong result for 'okay_ok1'")
        test.assert_equals(is_valid("$ok"), True, "Wrong result for '$ok'")
        test.assert_equals(is_valid("___"), True, "Wrong result for '___'")
        test.assert_equals(is_valid("str_STR"), True, "Wrong result for 'str_STR'")
        test.assert_equals(is_valid("myIdentf"), True, "Wrong result for 'myIdentf'")

    @test.it('should return false for invalid identifiers')
    def example_cases():
        test.assert_equals(is_valid("1ok0okay"), False, "Wrong result for '1ok0okay'")
        test.assert_equals(is_valid("!Ok"), False, "Wrong result for '!Ok'")
        test.assert_equals(is_valid(""), False, "Wrong result for an empty string")
        test.assert_equals(is_valid("str-str"), False, "Wrong result for 'str-str'")
        test.assert_equals(is_valid("no no"), False, "Wrong result for 'no no'")