import codewars_test as test
from kata import encrypt

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(encrypt("", 1), "")
        test.assert_equals(encrypt("a", 1), "b")
        test.assert_equals(encrypt("please encrypt me", 2), "rngcug\"gpet{rv\"og")