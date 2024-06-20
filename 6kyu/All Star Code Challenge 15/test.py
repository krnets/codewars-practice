import codewars_test as test
from kata import rotate

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("should output list with all possible rotations included")
    def _():
        test.assert_equals(rotate("Hello"), ["elloH", "lloHe", "loHel", "oHell", "Hello"])
    @test.it("should return [\" \"] when given \" \" as argument")
    def _():   
        test.assert_equals(rotate(" "), [" "])
    @test.it("should return [] when given \"\" as argument")
    def _():
        test.assert_equals(rotate(""),[])
    @test.it("Strings composed of digits are tested too")
    def _():
        test.assert_equals(rotate("123"), ["231", "312", "123"])
