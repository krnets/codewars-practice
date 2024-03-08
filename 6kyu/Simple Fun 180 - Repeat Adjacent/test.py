import codewars_test as test
from kata import repeat_adjacent

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(repeat_adjacent("ccccoodeffffiiighhhhhhhhhhttttttts"),3)
        test.assert_equals(repeat_adjacent("soooooldieeeeeer"),0)
        test.assert_equals(repeat_adjacent("ccccoooooooooooooooooooooooddee"),1)
        test.assert_equals(repeat_adjacent("wwwwaaaarrioooorrrrr"),2)
        test.assert_equals(repeat_adjacent("gztxxxxxggggggggggggsssssssbbbbbeeeeeeehhhmmmmmmmitttttttlllllhkppppp"),2)