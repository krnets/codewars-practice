from kata import latest_clock
import codewars_test as test


@test.describe("Example tests")
def example_tests():

    @test.it("latest_clock(1, 9, 8, 3) should return '19:38'")
    def test1():
        test.assert_equals(latest_clock(1, 9, 8, 3), "19:38")

    @test.it("latest_clock(9, 1, 2, 5) should return '21:59'")
    def test2():
        test.assert_equals(latest_clock(9, 1, 2, 5), "21:59")

    @test.it("latest_clock(0, 1, 9, 3) should return '19:30'")
    def test3():
        test.assert_equals(latest_clock(0, 1, 9, 3), "19:30")

    @test.it("latest_clock(0, 0, 5, 2) should return '20:50'")
    def test4():
        test.assert_equals(latest_clock(0, 0, 5, 2), "20:50")
