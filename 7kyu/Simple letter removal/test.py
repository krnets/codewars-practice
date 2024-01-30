import codewars_test as test
from kata import solve


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(solve("abracadabra", 1), "bracadabra")
        test.assert_equals(solve("abracadabra", 2), "brcadabra")
        test.assert_equals(solve("abracadabra", 6), "rcdbr")
        test.assert_equals(solve("abracadabra", 8), "rdr")
        test.assert_equals(solve("abracadabra", 50), "")
        test.assert_equals(solve("hxehmvkybeklnj", 5), "xmvkyklnj")
        test.assert_equals(solve("cccaabababaccbc", 3), "cccbbabaccbc")
        test.assert_equals(solve("cccaabababaccbc", 9), "cccccc")
        test.assert_equals(solve("u", 1), "")
        test.assert_equals(solve("back", 3), "k")
