import codewars_test as test
from kata import remove


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(remove("Hi!"), "Hi!")
        test.assert_equals(remove("Hi!!!"), "Hi!!!")
        test.assert_equals(remove("!Hi"), "Hi")
        test.assert_equals(remove("!Hi!"), "Hi!")
        test.assert_equals(remove("Hi! Hi!"), "Hi Hi!")
        test.assert_equals(remove("Hi"), "Hi")
        test.assert_equals(remove("MGXW!!!!N!JKZVW!NG!Y"), "MGXWNJKZVWNGY")
        test.assert_equals(remove("VPW!LMXF!!!H!DMA!MCO"), "VPWLMXFHDMAMCO")
        test.assert_equals(remove("!FM!!JCJGFLHXCO!FIEU"), "FMJCJGFLHXCOFIEU")
