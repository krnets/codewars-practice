import codewars_test as test
from kata import good_vs_evil


@test.it("Sample tests")
def sample_tests():
    test.assert_equals(
        good_vs_evil("1 1 1 1 1 1", "1 1 1 1 1 1 1"),
        "Battle Result: Evil eradicates all trace of Good",
    )
    test.assert_equals(
        good_vs_evil("0 0 0 0 0 10", "0 1 1 1 1 0 0"),
        "Battle Result: Good triumphs over Evil",
    )
    test.assert_equals(
        good_vs_evil("1 0 0 0 0 0", "1 0 0 0 0 0 0"),
        "Battle Result: No victor on this battle field",
    )
