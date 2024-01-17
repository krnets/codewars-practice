import random
import codewars_test as test
from kata import solution


def rand_type():
    r = random.randint(1, 5)
    if r == 1:
        return random.choice([True, False])
    elif r == 2:
        return random.randint(100, 200) + random.random()
    elif r == 3:
        ln = random.randint(0, 20)
        s = ""
        for _ in range(ln):
            s += random.choice(
                "abcdefghijklmnopqrstuvwxyz0123456789_+-=`~|][{;:,.<>!@#$%^&*()"
            )
        return s
    elif r == 4:
        r = random.randint(0, 100)
        while r in (4, 7):
            r = random.randint(0, 100)
        return r
    elif r == 5:
        return None


@test.describe("No Cheating")
def solution_check():
    @test.it("Some things shouldn't be used in your code...")
    def prescan_solution():
        with open("solution.py", "r") as file:
            solution = file.read()
        for x in "if eval exec match case else".split():
            test.expect(x not in solution, f"Your code isn't allowed to use {x!r}")


@test.describe("Tests for 4 and 7")
def _():
    for inp, exp in [(7, 4), (4, 7)]:

        @test.it(f"n = {inp} should return {exp}")
        def __():
            test.assert_equals(solution(inp), exp)


@test.describe("False-y Tests")
def _():
    @test.it("Random ints")
    def __():
        for ___ in range(100):
            r = random.randint(0, 100)
            while r in (4, 7):
                r = random.randint(0, 100)
            test.expect(not solution(r), f"n = {r} should be False-y")

    @test.it("Random other types")
    def __():
        for ___ in range(100):
            r = rand_type()
            test.expect(not solution(r), f"n = {r} should be False-y")
