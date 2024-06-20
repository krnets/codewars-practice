import codewars_test as test
from kata import alphabet_war

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(alphabet_war("z"),"Right side wins!")
        test.assert_equals(alphabet_war("****") , "Let's fight again!")
        test.assert_equals(alphabet_war("z*dq*mw*pb*s"), "Let's fight again!")
        test.assert_equals(alphabet_war("zdqmwpbs"), "Let's fight again!")
        test.assert_equals(alphabet_war("zz*zzs"), "Right side wins!")
        test.assert_equals(alphabet_war("sz**z**zs"), "Left side wins!")
        test.assert_equals(alphabet_war("z*z*z*zs"), "Left side wins!")
        test.assert_equals(alphabet_war("*wwwwww*z*"), "Left side wins!")
        test.assert_equals(alphabet_war("w****z") , "Let's fight again!")
        test.assert_equals(alphabet_war("mb**qwwp**dm") , "Let's fight again!")