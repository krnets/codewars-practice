import codewars_test as test
from kata import get_column_title

test.describe("Example tests")
actual = get_column_title(1)
expected = "A"
test.assert_equals(actual, expected)
test.assert_equals(get_column_title(26), "Z")
test.assert_equals(get_column_title(52), "AZ")
test.assert_equals(get_column_title(53), "BA")
test.assert_equals(get_column_title(702), "ZZ")
test.expect_error("Invalid type value should throw error.", lambda : get_column_title("15"))
test.expect_error("Invalid type value should throw error.", lambda : get_column_title())