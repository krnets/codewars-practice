import codewars_test as test
from kata import gaslighting


def do_test(args, expected):
    if expected:
        message = f"Your friend knows letters {list(args[2])} and CAN distinguish between `{args[0]}` and `{args[1]}`"
    else:
        message = f"Your friend knows letters {list(args[2])} and CANNOT distinguish between `{args[0]}` and `{args[1]}`"
    actual = gaslighting(*args)

    test.assert_equals(actual, expected, message)


@test.it("Example tests")
def _():
    do_test(("snack", "snake", "c"), True)
    do_test(("snack", "snack", "snack"), False)
    do_test(("snake", "snack", "c"), True)
    do_test(("ping", "pong", "png"), False)
    do_test(("ping", "pong", "i"), True)
