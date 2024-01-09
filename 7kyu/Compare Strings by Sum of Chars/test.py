import codewars_test as test
from kata import compare


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Simple Cases")
    def example_cases():
        test.assert_equals(compare("AD", "BC"), True, "'AD' vs 'BC'")
        test.assert_equals(compare("AD", "DD"), False, "'AD' vs 'DD'")
        test.assert_equals(compare("gf", "FG"), True, "'gf' vs 'FG'")
        test.assert_equals(compare("Ad", "DD"), False, "'Ad' vs 'DD'")
        test.assert_equals(compare("zz1", ""), True, "'zz1' vs ''")
        test.assert_equals(compare("ZzZz", "ffPFF"), True, "'ZzZz' vs 'ffPFF'")
        test.assert_equals(compare("kl", "lz"), False, "'kl' vs 'lz'")
        test.assert_equals(compare(None, ""), True, "'<null>' vs ''")
        test.assert_equals(compare("!!", "7476"), True, "'!!' vs '7476'")
        test.assert_equals(compare("##", "1176"), True, "'##' vs '1176'")
