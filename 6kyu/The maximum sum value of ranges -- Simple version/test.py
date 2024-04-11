from kata import max_sum
import codewars_test as test

@test.it("Basic test")
def basic_test():
    test.assert_equals(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,3],[0,4],[6,8]]), 6)
    test.assert_equals(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,3]]), 5)
    test.assert_equals(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,4],[2,5]]), 0)
    test.assert_equals(max_sum([11,-22,31,34,-45,-46,35,32,21], [[1,4],[0,3],[6,8],[0,8]]), 88)