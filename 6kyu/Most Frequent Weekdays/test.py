import codewars_test as test
from kata import most_frequent_days

test.describe("Example Tests")

test.assert_equals(most_frequent_days(2427), ['Friday'])
test.assert_equals(most_frequent_days(2185), ['Saturday'])
test.assert_equals(most_frequent_days(1770), ['Monday'])
test.assert_equals(most_frequent_days(1785), ['Saturday'])
test.assert_equals(most_frequent_days(1984), ['Monday', 'Sunday'])
test.assert_equals(most_frequent_days(2000), ['Saturday', 'Sunday'])
test.assert_equals(most_frequent_days(2516), ['Wednesday', 'Thursday'])