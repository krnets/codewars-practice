import codewars_test as test
from kata import is_a_valid_message

@test.describe("Fixed tests")
def test_group():
    @test.it("test1")
    def test_case():
        test.assert_equals(is_a_valid_message("3hey5hello2hi"), True)
        
    @test.it("test2")
    def test_case():
        test.assert_equals(is_a_valid_message("4code13hellocodewars"), True)
        
    @test.it("test3")
    def test_case():
        test.assert_equals(is_a_valid_message("3hey5hello2hi5"), False)
        
    @test.it("test4")
    def test_case():
        test.assert_equals(is_a_valid_message("code4hello5"), False)
        
    @test.it("test5")
    def test_case():
        test.assert_equals(is_a_valid_message("1a2bb3ccc4dddd5eeeee"), True)
        
    @test.it("test6")
    def test_case():
        test.assert_equals(is_a_valid_message(""), True)