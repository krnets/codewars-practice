from solve import get_number_from_string
import codewars_test as test

test.describe("Example Tests")
tests = (
    ("1", 1),
    ("123", 123),
    ("this is number: 7", 7),
    ("$100 000 000", 100000000),
    ("hell5o wor6ld", 56),
    ("one1 two2 three3 four4 five5", 12345),
)

for t in tests:
    inp, exp = t
    test.assert_equals(get_number_from_string(inp), exp)
