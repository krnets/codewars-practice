import codewars_test as test
from kata import time_correct


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("None or empty")
    def basic_test_cases():
        test.assert_equals(time_correct(None), None)
        test.assert_equals(time_correct(""), "")

    @test.it("Invalid Format")
    def basic_test_cases():
        test.assert_equals(time_correct("001122"), None)
        test.assert_equals(time_correct("00;11;22"), None)
        test.assert_equals(time_correct("0a:1c:22"), None)
        test.assert_equals(time_correct("24:78:+3"), None)

    @test.it("Correction Tests")
    def basic_test_cases():
        test.assert_equals(time_correct("09:10:01"), "09:10:01")
        test.assert_equals(time_correct("11:70:10"), "12:10:10")
        test.assert_equals(time_correct("19:99:99"), "20:40:39")
        test.assert_equals(time_correct("24:01:01"), "00:01:01")
        test.assert_equals(time_correct("52:01:01"), "04:01:01")
        test.assert_equals(time_correct("14:59:94"), "15:00:34")
        test.assert_equals(time_correct("14:60:34"), "15:00:34")


@test.describe("Random Tests")
def random_tests():
    from random import randint

    sol = (
        lambda t: ""
        if t == ""
        else (
            lambda h, m, s: "%s:%s:%s"
            % (
                ("0" + str((h + (1 if m > (59 if s < 60 else 58) else 0)) % 24))[-2:],
                ("0" + str((m + (1 if s > 59 else 0)) % 60))[-2:],
                ("0" + str(s % 60))[-2:],
            )
        )(*map(int, t.split(":")))
        if (
            type(t) == str
            and len(t) == 8
            and t.count(":") == 2
            and all(n.isdigit() for n in t.split(":"))
        )
        else None
    )
    base = ":;0123456789+/"

    for _ in range(40):
        t = "%s:%s:%s" % (
            ("0" + str(randint(1, 36)))[-2:],
            ("0" + str(randint(1, 99)))[-2:],
            ("0" + str(randint(1, 99)))[-2:],
        )
        t = t.replace(
            base[randint(0, len(base) - 1)],
            (lambda n: base[n] if n < len(base) else "")(randint(0, len(base))),
        )

        @test.it("Testing for " + repr(t))
        def basic_test_cases():
            test.assert_equals(
                time_correct(t), sol(t), "It should work for random inputs too"
            )
