import codewars_test as test
import itertools
import random
from kata import next_item

@test.describe('next_item')
def test_next_item():
    @test.it('should pass some tests')
    def tests():
        test.assert_equals(next_item([1, 2, 3, 4, 5, 6, 7, 8], 5), 6)
        test.assert_equals(next_item(['a', 'b', 'c'], 'd'), None)
        test.assert_equals(next_item(['a', 'b', 'c'], 'c'), None)
        test.assert_equals(next_item('testing', 't'), 'e')
        test.assert_equals(next_item(iter(range(1, 30000)), 12), 13)
        test.assert_equals(next_item('Hello!', 'o'), '!')
        test.assert_equals(next_item('Hello!', '!'), None)
        test.assert_equals(next_item('Hello!', 'x'), None)
    
    @test.it('should pass more interesting tests')
    def more_interesting_tests():
        test.assert_equals(next_item(itertools.count(1), 12), 13)
        test.assert_equals(next_item(iter(itertools.count(3)), 700), 701);
        for i in range(10):
            s, e = random.randint(3, 5), random.randint(0, 1499)
            test.assert_equals(
                next_item(iter(range(0, e, s)), 660),
                660 + s if 660 + s < e else None)
