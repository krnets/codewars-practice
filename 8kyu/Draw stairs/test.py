from random import randint as r
from kata import draw_stairs
import codewars_test as test

test.it("Fixed Tests")
stairs = '''I\n I\n  I'''
test.assert_equals(draw_stairs(3), stairs)
stairs = '''I\n I\n  I\n   I\n    I'''
test.assert_equals(draw_stairs(5), stairs)
test.it("30 Random Tests")


def draw(n):
    stairs = ''
    for x in range(n):
        stairs += ' '*x + 'I' + '\n'
    return stairs.rstrip('\n')


for x in range(30):
    num = r(1, 100)
    test.assert_equals(draw_stairs(num), draw(num))
