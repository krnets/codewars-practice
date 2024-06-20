import codewars_test as test
from kata import count_adjacent_pairs

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(count_adjacent_pairs(''), 0)
    test.assert_equals(count_adjacent_pairs('orange Orange kiwi pineapple apple'), 1)
    test.assert_equals(count_adjacent_pairs('banana banana banana'), 1)
    test.assert_equals(count_adjacent_pairs('banana banana banana terracotta banana terracotta terracotta pie!'), 2)
    test.assert_equals(count_adjacent_pairs('pineapple apple'), 0)