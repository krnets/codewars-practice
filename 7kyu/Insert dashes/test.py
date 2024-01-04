import codewars_test as test
from kata import insert_dash


@test.describe("Basic Tests")
def basic_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(insert_dash(454793), "4547-9-3")
        test.assert_equals(insert_dash(123456), "123456")
        test.assert_equals(insert_dash(1003567), "1003-567")
        test.assert_equals(insert_dash(24680), "24680")
        test.assert_equals(insert_dash(13579), "1-3-5-7-9")
