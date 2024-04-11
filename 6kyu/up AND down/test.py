import codewars_test as test
from kata import arrange
    
@test.describe("arrange")
def tests():
    def testing(actual, expected):
        test.assert_equals(actual, expected)
    @test.it("Basic tests")
    def basics():
        testing(arrange(""), "") # 0
        testing(arrange("who hit retaining The That a we taken"), "who RETAINING hit THAT a THE we TAKEN") # 3
        testing(arrange("on I came up were so grandmothers"), "i CAME on WERE up GRANDMOTHERS so") # 4
        testing(arrange("way the my wall them him"), "way THE my WALL him THEM") # 1
        testing(arrange("turn know great-aunts aunt look A to back"), "turn GREAT-AUNTS know AUNT a LOOK to BACK") # 2
