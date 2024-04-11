import codewars_test as test
from kata import cat_mouse


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(cat_mouse("..D.....C.m", 2), "Caught!")
        test.assert_equals(cat_mouse("............C.............D..m...", 8), "Escaped!")
        test.assert_equals(cat_mouse("m.C...", 5), "boring without all three")
        test.assert_equals(cat_mouse(".CD......m.", 10), "Protected!")
        test.assert_equals(cat_mouse(".CD......m.", 1), "Escaped!")
        test.assert_equals(cat_mouse("......m...C........D.", 20), "Caught!")
        test.assert_equals(cat_mouse("....D.............Cm", 17), "Caught!")
        test.assert_equals(cat_mouse(".D......C.m............", 11), "Caught!")
