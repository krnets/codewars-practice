import codewars_test as test
from kata import longest_palindrome


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(longest_palindrome("A"), 1)
        test.assert_equals(longest_palindrome("Hannah"), 6)
        test.assert_equals(longest_palindrome("xyz__a_/b0110//a_zyx"), 13)
        test.assert_equals(
            longest_palindrome("$aaabbbccddd_!jJpqlQx_.///yYabababhii_"), 25
        )
        test.assert_equals(longest_palindrome(""), 0)

    @test.it("Random Test Cases")
    def random_test_cases():
        test.assert_equals(
            longest_palindrome(
                "S7CJRHvwXej2f/ouhmWYA,.6gpx*i2gpbpGXP>le88EWub78sK>VNd-IAhCdsxGi5H=/<Fj,B97vy77H>X0Gt992Y0*SOH-QMq50hCO?S8u0aWYcAm!HJrF7gcof!=BG53!C3JQFj0T8Q4?5ABLIz.WF0<PCZA0,8Z1nP8aNsT6Us3KbwZi=OKkuMSdKh.ue*B?cNaA="
            ),
            165,
        )
