import codewars_test as test


def next_bigger(n):
    digits = list(str(n))
    i = j = len(digits) - 1
    while i > 0 and digits[i] <= digits[i - 1]:
        i -= 1
    if i == 0:
        return -1
    while digits[j] <= digits[i - 1]:
        j -= 1
    digits[i - 1], digits[j] = digits[j], digits[i - 1]
    digits[i:] = sorted(digits[i:])
    return int("".join(digits))


@test.describe("Sample tests")
def sample_tests():

    @test.it("Examples")
    def examples():
        test.assert_equals(next_bigger(1234567890), 1234567908)
        test.assert_equals(next_bigger(21), -1)
        test.assert_equals(next_bigger(12), 21)
        test.assert_equals(next_bigger(513), 531)
        test.assert_equals(next_bigger(2017), 2071)
        test.assert_equals(next_bigger(414), 441)
        test.assert_equals(next_bigger(144), 414)
