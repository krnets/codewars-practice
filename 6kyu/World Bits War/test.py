from kata import bits_war
import codewars_test as test

@test.describe("Basic tests")
def basic_tests():
    
    @test.it("Example tests")
    def example_tests():
        test.assert_equals(bits_war([1,5,12]), "odds win")
        test.assert_equals(bits_war([7,-3,20]), "evens win")
        test.assert_equals(bits_war([7,-3,-2,6]), "tie")
        test.assert_equals(bits_war([-3,-5]), "evens win")
        test.assert_equals(bits_war([]), "tie")