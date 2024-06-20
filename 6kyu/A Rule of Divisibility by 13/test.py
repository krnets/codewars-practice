import codewars_test as test
from kata import thirt
    
@test.describe("thirt")
def tests():
    @test.it("Fixed tests")
    def basics():
        test.assert_equals(thirt(8529), 79)
        test.assert_equals(thirt(85299258), 31)
        test.assert_equals(thirt(5634), 57)
        test.assert_equals(thirt(1111111111), 71)
        test.assert_equals(thirt(987654321), 30)
