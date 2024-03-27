import codewars_test as test
from random import randint as r
from kata import find_e as e


@test.describe("Example")
def test_group():
    @test.it("Fixed Tests")
    def test_case_fixed():
        test.assert_equals(e("actual"), 'There is no "e".')
        test.assert_equals(e("English"), "1")
        test.assert_equals(e("English exercise"), "4")
        test.assert_equals(e(""), "")
        test.assert_equals(e(None), None)
