import codewars_test as test
from kata import fill_gaps

test.assert_equals(
    fill_gaps([1, None, 1]),
    [1, 1, 1],
    "Replace None values surrounded by matching values",
)
test.assert_equals(
    fill_gaps([1, None, None, None, 1]), [1, 1, 1, 1, 1], "There may be multiple Nones"
)
test.assert_equals(
    fill_gaps([1, None, 1, 2, None, 2]),
    [1, 1, 1, 2, 2, 2],
    "There may be multiple replacements required",
)
test.assert_equals(
    fill_gaps([1, None, 2, None, 2, None, 1]),
    [1, None, 2, 2, 2, None, 1],
    "No nesting.",
)
test.assert_equals(
    fill_gaps([1, None, 2]), [1, None, 2], "No replacement if ends don't match"
)
test.assert_equals(
    fill_gaps([None, 1, None]),
    [None, 1, None],
    "No replacement if ends don't match off the ends of the array",
)
test.assert_equals(
    fill_gaps(
        ["codewars", None, None, "codewars", "real work", None, None, "real work"]
    ),
    [
        "codewars",
        "codewars",
        "codewars",
        "codewars",
        "real work",
        "real work",
        "real work",
        "real work",
    ],
    "Works with strings too",
)
