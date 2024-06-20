import codewars_test as test
from kata import convert_num

test.describe("Basic Tests")
test.it("Correctly converts to binary:")
test.assert_equals(convert_num(122, "bin"), "0b1111010")
test.it("Detects invalid number input:")
test.assert_equals(convert_num("dog", "bin"), "Invalid number input")
test.it("Correctly converts to hexadecimal:")
test.assert_equals(convert_num(0, "hex"), "0x0")
test.it("Detects invalid base input:")
test.assert_equals(convert_num(123, "lol"), "Invalid base input")
