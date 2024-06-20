from kata import box_capacity
import codewars_test as test

@test.describe("Box capacity test")
def box_capacity_test():
    
    @test.it("Examples")
    def examples():
        test.assert_equals(box_capacity(32, 64, 16), 13824)
        test.assert_equals(box_capacity(20, 20, 20), 3375)
        test.assert_equals(box_capacity(80, 40, 20), 27000)