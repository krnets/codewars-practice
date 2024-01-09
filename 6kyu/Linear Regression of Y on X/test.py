from random import randint
from solution import regressionLine
import codewars_test as test


@test.describe('Example Tests')
def example_tests():
    @test.it('Basic tests')
    def sample_test1():
        test.assert_equals(regressionLine([25, 30, 35, 40, 45, 50],
                                          [78, 70, 65, 58, 48, 42]),
                           (114.381, -1.4457))

    @test.it('Sample test 2')
    def sample_test2():
        test.assert_equals(regressionLine([25, 30, 35, 40, 45, 50],
                                          [78, 70, 65, 58, 48, 42]),
                           (114.381, -1.4457))
        test.assert_equals(regressionLine([56, 42, 72, 36, 63, 47, 55, 49, 38, 42, 68, 60],
                                          [147, 125, 160, 118, 149, 128, 150, 145, 115, 140, 152, 155]),
                           (80.7777, 1.138))
        test.assert_equals(regressionLine([0, 10, 20, 30, 40],
                                          [0.51, 0.55, 0.57, 0.59, 0.63]),
                           (0.514, 0.0028))


test.describe("Random tests")


def regressionLinesol(x, y):
    n = len(x)
    xSquare = [num ** 2 for num in x]
    ySquare = [num ** 2 for num in y]

    xy = [x[i] * y[i] for i in range(len(x))]
    a = (sum(xSquare) * sum(y) - sum(x) * sum(xy)) / \
        float((n * sum(xSquare) - (sum(x))**2))
    b = (n * sum(xy) - sum(x) * sum(y)) / \
        float((n * sum(xSquare) - (sum(x))**2))
    return round(a, 4), round(b, 4)


for i in range(40):
    testlen = randint(5, 15)
    testx, testy = [], []
    for j in range(testlen):
        testx += [randint(0, 100)]
        testy += [randint(0, 100)]
    test.it("Testing random array x: ["+(", ").join(map(str,
            testx))+"] and y: ["+(", ").join(map(str, testy))+"]")
    test.assert_equals(regressionLine(testx, testy), regressionLinesol(
        testx, testy), "It should work for random tests too")
