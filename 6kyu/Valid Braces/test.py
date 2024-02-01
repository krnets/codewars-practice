import codewars_test as test
from kata import valid_braces

def assert_valid(string):
    test.assert_equals(valid_braces(string), True, 'Expected "{0}" to be valid'.format(string))

def assert_invalid(string):
    test.assert_equals(valid_braces(string), False, 'Expected "{0}" to be invalid'.format(string))


@test.describe("Valid Braces")
def tests():
	@test.it("sample Tests")
	def sample_tests():
		assert_valid( "()" )
		assert_invalid( "(}" )
		assert_valid( "[]" )
		assert_invalid("[(])")
		assert_valid( "{}" )
		assert_valid( "{}()[]" )
		assert_valid( "([{}])" )
		assert_invalid( "([}{])" )
		assert_valid( "{}({})[]" )
		assert_valid( "(({{[[]]}}))" )
		assert_invalid( "(((({{" )
		assert_invalid( ")(}{][" )
		assert_invalid( "())({}}{()][][" )