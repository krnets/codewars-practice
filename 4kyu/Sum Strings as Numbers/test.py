import random
import codewars_test as test
from string import digits
from kata import sum_strings


@test.describe("Basic tests")
def test_examples():

    @test.it("Example tests")
    def basic_tests():
        test.assert_equals(sum_strings("1", "1"), "2")
        test.assert_equals(sum_strings("123", "456"), "579")


def rand_str_num():
    return "".join(random.choice(digits) for _ in range(random.randint(0, 1000)))


def __this_is_the_sol(x, y):
    out, ret = "", 0

    for c_x, c_y in zip(x.zfill(len(y))[::-1], y.zfill(len(x))[::-1]):
        ret, d = divmod(int(c_x) + int(c_y) + ret, 10)
        out += str(d)

    out = f"{out}{'1' * ret}"[::-1] or "0"
    return out if len(out) < 2 else out.lstrip("0")


@test.describe("Basic tests")
def test_examples():

    @test.it("Example tests")
    def basic_tests():
        test.assert_equals(sum_strings("1", "1"), "2")
        test.assert_equals(sum_strings("123", "456"), "579")

    @test.it("Fixed tests")
    def basic_test():
        test.assert_equals(sum_strings("10", "20"), "30")
        test.assert_equals(sum_strings("200", "100"), "300")

        test.assert_equals(sum_strings("99", "1"), "100")
        test.assert_equals(sum_strings("42", "69"), "111")

        test.assert_equals(sum_strings("2999", "302"), "3301")
        test.assert_equals(sum_strings("800", "9567"), "10367")

        test.assert_equals(sum_strings("00103", "08567"), "8670")
        test.assert_equals(sum_strings("0", "0"), "0")

        test.assert_equals(sum_strings("0", "5"), "5")
        test.assert_equals(sum_strings("5", "0"), "5")

        test.assert_equals(sum_strings("0", ""), "0")
        test.assert_equals(sum_strings("", ""), "0")

        test.assert_equals(sum_strings("9999", ""), "9999")
        test.assert_equals(sum_strings("", "9999"), "9999")

        test.assert_equals(sum_strings("9999999999999999", "1"), "10000000000000000")
        test.assert_equals(sum_strings("1", "9999999999999999"), "10000000000000000")

        test.assert_equals(
            sum_strings("712569312664357328695151392", "8100824045303269669937"),
            "712577413488402631964821329",
        )

        test.assert_equals(
            sum_strings(
                "50095301248058391139327916261", "81055900096023504197206408605"
            ),
            "131151201344081895336534324866",
        )

    @test.it("Random tests")
    def basic_test():
        x = rand_str_num()
        y = rand_str_num()

        for _ in range(100):
            test.assert_equals(sum_strings(x, y), __this_is_the_sol(x, y))

    @test.it("Is it fast enough?")
    def basic_test():
        x = str(random.randint(10, 99)) * random.randint(1_000_000, 1_100_000)
        y = str(random.randint(10, 99)) * random.randint(1_000_000, 1_100_000)

        test.expect(sum_strings(x, y) == __this_is_the_sol(x, y), "big test failed")
