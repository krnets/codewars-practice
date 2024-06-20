import codewars_test as test
from kata import comes_after

@test.describe('Example Tests')
def example_tests():
    @test.it('Example Test Case')
    def example_test_case():
        test.assert_equals(comes_after("Pirates say arrrrrrrrr.", 'r'), 'arrrrrrrr')
        test.assert_equals(comes_after("Free coffee for all office workers!", 'F'), 'rfeofi')
        test.assert_equals(comes_after("king kUnta is the sickest rap song ever kNown k!", 'k'),'iUeN') 
        test.assert_equals(comes_after("p8tice makes pottery p0rfect!", 'p'), 'o')
        test.assert_equals(comes_after("d8u d._ rly 2d1s", 'D'), '')
        test.assert_equals(comes_after("nothing to be found here", 'z'), '')