import codewars_test as test


def dig_pow(n, p):
    q = sum(int(c) ** (i + p) for i, c in enumerate(str(n)))
    return (-1, q // n)[q % n == 0]


@test.describe("Fixed tests")
def fixed_test():
    @test.it("Samples")
    def sample_tests():
        test.assert_equals(dig_pow(89, 1), 1)
        test.assert_equals(dig_pow(92, 1), -1)
        test.assert_equals(dig_pow(46288, 3), 51)
        test.assert_equals(dig_pow(41, 5), 25)
        test.assert_equals(dig_pow(114, 3), 9)
        test.assert_equals(dig_pow(8, 3), 64)
