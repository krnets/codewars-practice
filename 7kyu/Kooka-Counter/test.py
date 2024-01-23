import codewars_test as test
from kata import kooka_counter


@test.describe("Basic tests")
def test_group():
    @test.it("Should work for basic tests")
    def test_case():
        for inp, exp in (
            ("", 0),
            ("hahahahaha", 1),
            ("hahahahahaHaHaHa", 2),
            ("HaHaHahahaHaHa", 3),
            ("hahahahahahahaHaHa", 2),
        ):
            test.assert_equals(
                kooka_counter(inp), exp, f"Testing kooka_counter({inp!r})"
            )
