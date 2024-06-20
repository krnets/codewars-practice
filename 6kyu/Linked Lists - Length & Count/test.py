from random import randrange as rnd
import codewars_test as test
from kata import *


@test.describe("Tests")
def check():
    @test.it("tests for counting the length of a linked list.")
    def f():
        list = build_one_two_three()
        test.assert_equals(length(None), 0, "Length of null list should be zero.")
        test.assert_equals(
            length(Node(99)), 1, "Length of single node list should be one."
        )
        test.assert_equals(
            length(list), 3, "Length of the three node list should be three."
        )

    @test.it("tests for counting occurrences of a particular integer in a linked list.")
    def f():
        list = build_one_two_three()
        test.assert_equals(count(list, 1), 1, "list should only contain one 1.")
        test.assert_equals(count(list, 2), 1, "list should only contain one 2.")
        test.assert_equals(count(list, 3), 1, "list should only contain one 3.")
        test.assert_equals(
            count(list, 99), 0, "list should return zero for integer not found in list."
        )
        test.assert_equals(
            count(None, 1), 0, "null list should always return count of zero."
        )

    @test.it(
        "tests for counting multiple occurrences of a particular integer in a linked list."
    )
    def f():
        list = build_nodes([1, 1, 1, 2, 2, 2, 2, 3, 3])
        test.assert_equals(count(list, 1), 3, "list should contain three 1's.")
        test.assert_equals(count(list, 2), 4, "list should contain four 2's.")
        test.assert_equals(count(list, 3), 2, "list should contain two 3's.")

    def rnd_list(size):
        return [rnd(size) for n in range(rnd(size))]

    @test.it("random tests: length")
    def rf():
        def ref_len(xs):
            return len(xs)

        for i in range(1, 101):
            xs = rnd_list(i)
            actual = length(build_nodes(xs))
            expected = ref_len(xs)
            test.assert_equals(
                actual,
                expected,
                f"length( {' -> '.join([str(v) for v in xs] + ['None'])} )",
            )

    @test.it("random tests: count")
    def rf():
        def ref_count(xs, x):
            return len([y for y in xs if y == x])

        for i in range(1, 101):
            xs = rnd_list(i)
            x = rnd(i)
            actual = count(build_nodes(xs), x)
            expected = ref_count(xs, x)
            test.assert_equals(
                actual,
                expected,
                f"count( {' -> '.join([str(v) for v in xs] + ['None'])}, {x} )",
            )
