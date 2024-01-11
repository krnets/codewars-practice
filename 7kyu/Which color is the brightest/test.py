from kata import brightest
import codewars_test as test


def dotest(colors, expected):
    actual = brightest(colors[:])
    test.assert_equals(
        actual,
        expected,
        f'Test failed\nWith colors = {colors}\nExpected "{expected}" but got "{actual}"',
    )


@test.describe("Fixed tests")
def fixed_tests():
    @test.it("Basic tests")
    def test_basic():
        dotest(["#001000", "#000000"], "#001000")
        dotest(["#ABCDEF", "#123456"], "#ABCDEF")
        dotest(["#00FF00", "#FFFF00"], "#00FF00")
        dotest(["#FFFFFF", "#1234FF"], "#FFFFFF")
        dotest(["#FFFFFF", "#123456", "#000000"], "#FFFFFF")
