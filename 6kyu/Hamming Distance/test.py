import codewars_test as test
from kata import hamming

@test.describe("Sample tests")
def sample_tests():
    
    @test.it("Sample tests")
    def sample_tests():
        test.assert_equals(hamming("hello world","hello tokyo"),4)
        test.assert_equals(hamming("a man a plan a canal","a man a plan sobanal"),3)
        test.assert_equals(hamming("hamming and cheese","Hamming and Cheese"),2)
        test.assert_equals(hamming("espresso","Expresso"),2)
        test.assert_equals(hamming("old father, old artificer","of my soul the uncreated "),24);