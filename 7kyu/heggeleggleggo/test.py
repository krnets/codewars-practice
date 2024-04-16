import codewars_test as test
from kata import heggeleggleggo

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(heggeleggleggo("hello"), "heggeleggleggo")
        test.assert_equals(heggeleggleggo("code here"), "ceggodegge heggeregge")
        test.assert_equals(heggeleggleggo("FUN KATA"), "FeggUNegg KeggATeggA")
        test.assert_equals(heggeleggleggo("egg"), "egegggegg")
        test.assert_equals(heggeleggleggo("Hello world"), "Heggeleggleggo weggoreggleggdegg")
        test.assert_equals(heggeleggleggo("scrambled eggs"), "seggceggreggameggbeggleggedegg egegggeggsegg")
        test.assert_equals(heggeleggleggo("eggy bread"), "egegggeggyegg beggreggeadegg")
