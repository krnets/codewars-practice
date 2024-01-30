import codewars_test as test
from kata import solution


@test.describe("Sample tests")
def sample_tests():
    @test.it("Test 1")
    def test_1():
        test.assert_equals(solution("RGBRGBRGGB"), 1)

    @test.it("Test 2")
    def test_2():
        test.assert_equals(solution("RGGRGBBRGRR"), 3)

    @test.it("Test 3")
    def test_3():
        test.assert_equals(solution("RRRRGGGGBBBB"), 9)
