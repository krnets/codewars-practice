import codewars_test as test
from kata import compress

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(compress("The bumble bee"), "012")
        test.assert_equals(compress("SILLY LITTLE BOYS silly little boys"), "012012")
        test.assert_equals(compress("Ask not what your COUNTRY can do for you ASK WHAT YOU CAN DO FOR YOUR country"), "01234567802856734")
        test.assert_equals(compress("The number 0 is such a strange number Strangely it has zero meaning"), "012345617891011")