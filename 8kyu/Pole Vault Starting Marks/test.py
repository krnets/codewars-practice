from random import randint
import codewars_test as test
from kata import starting_mark

test.describe("Basic tests")
test.assert_equals(starting_mark(1.52), 9.45)
test.assert_equals(starting_mark(2.83), 10.67)
test.assert_equals(starting_mark(1.22), 8.27)
test.assert_equals(starting_mark(2.13), 11.85)
test.assert_equals(starting_mark(1.75), 10.36)

test.describe("Random tests")
def sol(h): return round(9.45+(h-1.52)*1.22/0.31, 2)


for _ in range(40):
    h = randint(122, 213)/100.0
    test.it("Testing for "+repr(h))
    test.assert_equals(starting_mark(h), sol(h), "It should work for random inputs too")sol = lambda h: round(9.45+(h-1.52)*1.22/0.31, 2)

for _ in range(40):
    h = randint(122, 213)/100.0
    test.it("Testing for "+repr(h))
    test.assert_equals(starting_mark(h), sol(
        h), "It should work for random inputs too")
