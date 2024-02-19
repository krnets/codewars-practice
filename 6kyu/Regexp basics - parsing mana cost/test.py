import codewars_test as test
from kata import parse_mana_cost

test.describe("Basic tests")
test.assert_equals(parse_mana_cost(""), {})
test.assert_equals(parse_mana_cost("0"), {})
test.assert_equals(parse_mana_cost("1"), {"*": 1})
test.assert_equals(parse_mana_cost("4"), {"*": 4})
test.assert_equals(parse_mana_cost("15"), {"*": 15})
test.assert_equals(parse_mana_cost("2rr"), {"*": 2, "r": 2})
test.assert_equals(parse_mana_cost("1wbg"), {"*": 1, "w": 1, "b": 1, "g": 1})
test.assert_equals(parse_mana_cost("1WWU"), {"*": 1, "w": 2, "u": 1})

test.describe("Edge tests")
test.assert_equals(parse_mana_cost("0r"), {"r": 1})
test.assert_equals(parse_mana_cost("2x"), None)
test.assert_equals(parse_mana_cost("2R"), {"*": 2, "r": 1})
test.assert_equals(parse_mana_cost("2\n"), None)
test.assert_equals(parse_mana_cost("\n2"), None)
