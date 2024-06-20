import codewars_test as test
from kata import char_concat

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(char_concat("abc def"), 'af1be2cd3', "Should work for example test")
        test.assert_equals(char_concat("CodeWars"), 'Cs1or2da3eW4', "Should work for 'CodeWars'")
        test.assert_equals(char_concat("CodeWars Rocks"), 'Cs1ok2dc3eo4WR5a 6rs7', "Should work for two words, like 'CodeWars Rocks'")
        test.assert_equals(char_concat("1234567890"), '101292383474565', "Should work for numbers")