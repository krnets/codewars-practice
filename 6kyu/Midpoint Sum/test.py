import codewars_test as test
from kata import midpoint_sum

test.describe("Normal Cases")
test.expect(midpoint_sum([4,1,7,9,3,9]) == 3, "[4,1,7,9,3,9] should return 3")
test.expect(midpoint_sum([1,0,1]) == 1, "[1,0,1] should equal 1")
test.expect(midpoint_sum([9,0,1,2,3,4]) == 2, "[9,0,1,2,3,4] should equal 2")
test.expect(midpoint_sum([0,0,4,0]) == 2, "[0,0,4,0] should equal 2")
test.expect(midpoint_sum([-10,3,7,8,-6,-13,21]) == 4, "[-10,3,7,8,-6,-13,21] should equal 4")
test.expect(midpoint_sum([1,1,1,1,-5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) ==  52, "Large valid sequence: [1,1,1,1,-5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] should equal 52")
