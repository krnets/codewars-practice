import codewars_test as test
from kata import bits_battle

@test.describe('sample tests')
def sample_tests() :
	@test.it('should work for some sample tests')
	def do_sample_tests():
		test.assert_equals(bits_battle([5, 3, 14]), 'odds win')
		test.assert_equals(bits_battle([3, 8, 22, 15, 78]), 'evens win')
		test.assert_equals(bits_battle([]), 'tie')
		test.assert_equals(bits_battle([1, 13, 16]), 'tie')
		test.assert_equals(bits_battle([0]), 'tie')
		test.assert_equals(bits_battle([0, 1, 2]), 'tie')