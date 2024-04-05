import codewars_test as test
from kata import encode

@test.describe('Basic tests')
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(encode("Hello World!"),"10110 00111!")