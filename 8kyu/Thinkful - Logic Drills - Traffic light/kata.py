from itertools import cycle
import codewars_test as test


def update_light(current):
    lights = cycle(["green", "yellow", "red"])
    while True:
        if current == next(lights):
            return next(lights)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(update_light("green"), "yellow")
        test.assert_equals(update_light("yellow"), "red")
        test.assert_equals(update_light("red"), "green")
