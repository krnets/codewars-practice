import codewars_test as test
from kata import number_of_pairs

@test.describe("Basic tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(number_of_pairs(["red","red"]),1)
        test.assert_equals(number_of_pairs(["red","green","blue"]),0)
        test.assert_equals(number_of_pairs(["gray","black","purple","purple","gray","black"]),3)
        test.assert_equals(number_of_pairs([]),0)
        test.assert_equals(number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]),4)