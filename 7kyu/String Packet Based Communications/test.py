import codewars_test as test
from kata import communication_module

test.assert_equals(communication_module("H1H10F1200120008F4F4"), "H1H1FFFF00200000F4F4")
test.assert_equals(communication_module("X7X7B7A201400058L0L0"), "X7X7FFFF00820000L0L0")
test.assert_equals(communication_module("R5R5C3D900120008K4K4"), "R5R5FFFF00960000K4K4")