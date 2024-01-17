import codewars_test as test
from kata import scrolling_text

test.assert_equals(scrolling_text("abc"), ["ABC", "BCA", "CAB"])
test.assert_equals(
    scrolling_text("codewars"),
    [
        "CODEWARS",
        "ODEWARSC",
        "DEWARSCO",
        "EWARSCOD",
        "WARSCODE",
        "ARSCODEW",
        "RSCODEWA",
        "SCODEWAR",
    ],
)
