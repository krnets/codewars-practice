import codewars_test as test
from kata import total_bill

@test.describe("Sample tests")
def tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(total_bill('rr'), 4)
        test.assert_equals(total_bill('rr rrr'), 8)
        test.assert_equals(total_bill('rr rrr rrr rr'), 16)
        test.assert_equals(total_bill('rrrrrrrrrrrrrrrrrr   rr r'), 34)
        test.assert_equals(total_bill(''), 0)