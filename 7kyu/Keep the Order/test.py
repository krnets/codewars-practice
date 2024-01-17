import codewars_test as test
from kata import keep_order


@test.describe("Example tests")
def test_group():
    @test.it("Fixed cases")
    def test_case():
        test.assert_equals(
            keep_order([1, 2, 3, 4, 7], 5), 4, "Testing keep_order([1, 2, 3, 4, 7], 5)"
        )
        test.assert_equals(
            keep_order([1, 2, 3, 4, 7], 0), 0, "Testing keep_order([1, 2, 3, 4, 7], 0)"
        )
        test.assert_equals(
            keep_order([1, 1, 2, 2, 2], 2), 2, "Testing keep_order([1, 1, 2, 2, 2], 2)"
        )
        test.assert_equals(
            keep_order([1, 2, 3, 4], 5), 4, "Testing keep_order([1, 2, 3, 4], 5)"
        )
        test.assert_equals(
            keep_order([1, 2, 3, 4], -1), 0, "Testing keep_order([1, 2, 3, 4], -1)"
        )
        test.assert_equals(
            keep_order([1, 2, 3, 4], 2), 1, "Testing keep_order([1, 2, 3, 4], 2)"
        )
        test.assert_equals(
            keep_order([1, 2, 3, 4], 0), 0, "Testing keep_order([1, 2, 3, 4], 0)"
        )
        test.assert_equals(
            keep_order([1, 2, 3, 4], 1), 0, "Testing keep_order([1, 2, 3, 4], 1)"
        )
        test.assert_equals(
            keep_order([1, 2, 3, 4], 2), 1, "Testing keep_order([1, 2, 3, 4], 2)"
        )
        test.assert_equals(
            keep_order([1, 2, 3, 4], 3), 2, "Testing keep_order([1, 2, 3, 4], 3)"
        )
