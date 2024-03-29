import codewars_test as test
from kata import permute_a_palindrome


@test.describe("Sample tests")
def sample_tests():

    @test.it("input = a")
    def sample_test1():
        test.assert_equals(permute_a_palindrome("a"), True)

    @test.it("input = aa")
    def sample_test2():
        test.assert_equals(permute_a_palindrome("aa"), True)

    @test.it("input = aaa")
    def sample_test3():
        test.assert_equals(permute_a_palindrome("aaa"), True)

    @test.it("input = baa")
    def sample_test4():
        test.assert_equals(permute_a_palindrome("baa"), True)

    @test.it("input = aab")
    def sample_test5():
        test.assert_equals(permute_a_palindrome("aab"), True)

    @test.it("input = baabcd")
    def sample_test6():
        test.assert_equals(permute_a_palindrome("baabcd"), False)

    @test.it("input = racecars")
    def sample_test7():
        test.assert_equals(permute_a_palindrome("racecars"), False)

    @test.it("input = abcdefghba")
    def sample_test8():
        test.assert_equals(permute_a_palindrome("abcdefghba"), False)

    @test.it("input is an empty string")
    def sample_test9():
        test.assert_equals(permute_a_palindrome(""), True)

    @test.it("small fixed tests")
    def sample_test10():
        test.assert_equals(permute_a_palindrome("aa"), True)
        test.assert_equals(
            permute_a_palindrome(
                "xxhawslwkrstwtiuwvxzdtwthstwkstdlfwxxiwuzfoftrotvccxaf"
            ),
            True,
        )
        test.assert_equals(
            permute_a_palindrome(
                "kdhravekkkofjihdkorzuxlwdzxqmeundwdljhfmnskuswiiwaeacihyigzyjqhhixepfbkbkzndwybkuohfqpbpv"
            ),
            False,
        )
        test.assert_equals(
            permute_a_palindrome("baabcd"),
            False,
        )
        test.assert_equals(
            permute_a_palindrome("racecars"),
            False,
        )
        test.assert_equals(
            permute_a_palindrome("abcdefghba"),
            False,
        )
        test.assert_equals(
            permute_a_palindrome("bgotizv"),
            False,
        )