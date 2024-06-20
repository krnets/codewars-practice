import codewars_test as test
from kata import cookie


@test.describe("Basic tests")
def basic_tests():

    @test.it("Examples")
    def examples():
        test.assert_equals(cookie("Ryan"), "Who ate the last cookie? It was Zach!")
        test.assert_equals(cookie(2.3), "Who ate the last cookie? It was Monica!")
        test.assert_equals(cookie(26), "Who ate the last cookie? It was Monica!")
        test.assert_equals(cookie(True), "Who ate the last cookie? It was the dog!")
