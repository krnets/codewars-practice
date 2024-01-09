import codewars_test as test
from kata import circle_area, Circle, Point


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(
            round(circle_area(Circle(Point(10, 10), 30)), 6), 2827.433388)
        test.assert_equals(
            round(circle_area(Circle(Point(25, -70), 30)), 6), 2827.433388)
        test.assert_equals(round(circle_area(Circle(Point(-15, 5), 0)), 6), 0)
        test.assert_equals(
            round(circle_area(Circle(Point(-15, 5), 12.5)), 6), 490.873852)


@test.describe('Random tests')
def random_tests():
    from random import randint

    for i in range(100):
        ca = Point(randint(-50, 50), randint(-50, 50))
        ra = randint(0, 50)
        a = Circle(ca, ra)
        actual = circle_area(a)
        expected = 3.141592653589793 * ra**2

        @test.it(f"testing for circle_area({a})")
        def test_case():
            test.assert_equals(round(actual, 6), round(expected, 6))
