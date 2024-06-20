import codewars_test as test


def alt_or(lst):
    if not lst:
        return None
    ans = lst[0]

    for x in lst[1:]:
        match (x, ans):
            case (False, False): ans = False
            case _: ans = True
    return ans


@test.describe("Alternate Logic")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(alt_or([]), None)
        test.assert_equals(alt_or([False, False, False, False, False, False]), False)
        test.assert_equals(alt_or([False, False, False, False, False, True]), True)
        test.assert_equals(alt_or([False, False, False, False, True, False]), True)
        test.assert_equals(alt_or([False, False, False, False, True, True]), True)
        test.assert_equals(alt_or([False, False, False, True, False, False]), True)
        test.assert_equals(alt_or([False, False, False, True, False, True]), True)
        test.assert_equals(alt_or([False, False, False, True, True, False]), True)
        test.assert_equals(alt_or([False, False, False, True, True, True]), True)
        test.assert_equals(alt_or([False, False, True, False, False, False]), True)
        test.assert_equals(alt_or([False, False, True, False, False, True]), True)
        test.assert_equals(alt_or([False, False, False, False]), False)
        test.assert_equals(alt_or([False, False, False]), False)
        test.assert_equals(alt_or([False, False]), False)
        test.assert_equals(alt_or([False]), False)
