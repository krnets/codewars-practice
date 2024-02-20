import codewars_test as test
from kata import find_middle


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(find_middle(None), -1)
        test.assert_equals(find_middle([1, 2, 3]), -1)
        test.assert_equals(find_middle("s7d8jd9"), 0)
        test.assert_equals(find_middle("58jd9fgh/fgh6s.,sdf"), 16)
        test.assert_equals(find_middle("pn*5*+-dhgy)*b<.@4wfs,fh}a+}e"), 20)
        test.assert_equals(find_middle("q~`q>$t<s]yl{%h!c@ew%!9y=rc8n~"), 72)
        test.assert_equals(find_middle(",qr1x_!5_(i]c*gshu}e&_(.$r)+3."), 15)
        test.assert_equals(find_middle(">ct`s()-}|2yqr[#[t^,av!]we5-fo"), 10)
        test.assert_equals(find_middle("mczd3!xs[+p1*/w*<^?4`loiwgr-7w"), 84)
