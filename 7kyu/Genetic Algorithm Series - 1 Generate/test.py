import codewars_test as test
from kata import generate


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(len(generate(0)), 0)
        test.assert_equals(len(generate(1)), 1)
        test.assert_equals(len(generate(16)), 16)
        test.assert_equals(len(generate(32)), 32)
        test.assert_equals(len(generate(64)), 64)
        test.assert_equals(len(generate(10000)), 10000)
        test.assert_equals(len(generate(1000000)), 1000000)


@test.describe("In chromosome of length 50")
def fixed_tests():
    @test.it("It should (probably) have at least one 1")
    def basic_test_cases():
        test.expect("1" in generate(50))

    @test.it("It should (probably) have at least one 0")
    def basic_test_cases():
        test.expect("0" in generate(50))


@test.describe("Random Tests")
def random_tests():
    from random import randint

    l = randint(10, 30)

    @test.it(
        "In a chromosome of length {}, running enough times it should be able to return all 2^{} possibilities ({})".format(
            l, l, 2**l
        )
    )
    def _():
        s = [generate(l) for _ in range(2000)]
        for i in range(l):
            test.expect(any([x[i] == "0" for x in s]) and any([x[i] == "1" for x in s]))
