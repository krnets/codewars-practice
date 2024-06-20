import codewars_test as test
from kata import last_non_empty_string


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Example Tests")
    def example_tests():
        test.assert_equals(last_non_empty_string("aabcbbca"), "ba")
        test.assert_equals(last_non_empty_string("abcd"), "abcd")
        test.assert_equals(last_non_empty_string("zzxdccvzdd"), "zd")
