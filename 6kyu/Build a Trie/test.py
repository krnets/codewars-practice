import codewars_test as test
from kata import build_trie

test.describe("Sample Tests")

test_data = {
    tuple(): {},
    ("",): {},
    ("trie",): {"t": {"tr": {"tri": {"trie": None}}}},
    ("tree",): {"t": {"tr": {"tre": {"tree": None}}}},
    ("trie", "trie"): {"t": {"tr": {"tri": {"trie": None}}}},
    ("A", "to", "tea", "ted", "ten", "i", "in", "inn"): {
        "A": None,
        "t": {"to": None, "te": {"tea": None, "ted": None, "ten": None}},
        "i": {"in": {"inn": None}},
    },
    ("true", "trust"): {"t": {"tr": {"tru": {"true": None, "trus": {"trust": None}}}}},
}

for test_input, expected in sorted(test_data.items()):
    test.assert_equals(build_trie(*test_input), expected)
