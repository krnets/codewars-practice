import codewars_test as test
from kata import missing

@test.describe("Basic Tests")
def test_group():
    @test.it("Should work for basic tests")
    def test_case():
        test.assert_equals(missing([0, 3, 5], "I love you"), "ivy")
        test.assert_equals(missing([29, 31, 8], "The quick brown fox jumps over the lazy dog"), "bay")
        test.assert_equals(missing([12, 4, 6], "Good Morning"), "No mission today")