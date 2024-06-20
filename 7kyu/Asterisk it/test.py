import codewars_test as test
from kata import asterisc_it

@test.describe('Example Tests')
def example_tests():        
    test.assert_equals(asterisc_it(5312708), '531270*8')
    test.assert_equals(asterisc_it(9682135), '96*8*2135')
    test.assert_equals(asterisc_it(2222), '2*2*2*2')
    test.assert_equals(asterisc_it(1111), '1111')
    test.assert_equals(asterisc_it(9999), '9999')
    test.assert_equals(asterisc_it('0000'), '0*0*0*0')
    test.assert_equals(asterisc_it(8), '8')
    test.assert_equals(asterisc_it(2), '2')
    test.assert_equals(asterisc_it(0), '0')
    test.assert_equals(asterisc_it([1, 4, 64, 68, 67, 23, 1]), '14*6*4*6*8*67231')