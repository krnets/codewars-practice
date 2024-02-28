import codewars_test as test
from kata import reverse

test.assert_equals(
    reverse(["I", "like", "big", "butts", "and", "I", "cannot", "lie!"]),
    ["!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"],
)

test.assert_equals(
    reverse(
        [
            "?kn",
            "ipnr",
            "utotst",
            "ra",
            "tsn",
            "iksr",
            "uo",
            "yer",
            "ofebta",
            "eote",
            "vahu",
            "oyodpm",
            "ir",
            "hsyn",
            "amwoH",
        ]
    ),
    [
        "How",
        "many",
        "shrimp",
        "do",
        "you",
        "have",
        "to",
        "eat",
        "before",
        "your",
        "skin",
        "starts",
        "to",
        "turn",
        "pink?",
    ],
)
