import codewars_test as test
from kata import solution


@test.describe("Example tests")
def test_group():
    @test.it("Basic tests")
    def test_case():
        test.assert_equals(solution(1, 1), [1], "Testing solution(1,1)")
        test.assert_equals(
            solution(123767, 4), [3, 7, 6, 7], "Testing solution(123767,4)"
        )
        test.assert_equals(solution(0, 1), [0], "Testing solution(0,1)")
        test.assert_equals(
            solution(34625647867585, 10),
            [5, 6, 4, 7, 8, 6, 7, 5, 8, 5],
            "Testing solution(34625647867585,10)",
        )

    @test.it("d <= 0")
    def test_case():
        test.assert_equals(solution(1234, 0), [], "Testing solution(1234,0)")
        test.assert_equals(solution(24134, -4), [], "Testing solution(24134,-4)")

    @test.it("d > number of digits in n")
    def test_case():
        test.assert_equals(solution(1343, 5), [1, 3, 4, 3], "Testing solution(1343,5)")
