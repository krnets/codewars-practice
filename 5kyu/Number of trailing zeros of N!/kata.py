import codewars_test as test


# def zeros(n):
#     if n < 5:
#         return 0
#     n //= 5
#     return n + zeros(n)


def zeros(n):
    res = 0
    while n:
        n //= 5
        res += n
    return res


@test.describe("Sample Tests")
def sample_tests():

    @test.it("Should pass sample tests")
    def sample_tests():
        test.assert_equals(zeros(0), 0, "Testing with n = 0")
        test.assert_equals(zeros(6), 1, "Testing with n = 6")
        test.assert_equals(zeros(30), 7, "Testing with n = 30")
        test.assert_equals(zeros(100), 24, "Testing with n = 100")
        test.assert_equals(zeros(1000), 249, "Testing with n = 1000")
        test.assert_equals(zeros(100000), 24999, "Testing with n = 100000")
        test.assert_equals(zeros(1000000000), 249999998, "Testing with n = 1000000000")
