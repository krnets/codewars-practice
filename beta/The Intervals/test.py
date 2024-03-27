from kata import the_intervals
import codewars_test as test


@test.describe('fixed tests')
def tests():
    
    @test.it('fixed_simple_tests')
    def tests():
        test.assert_equals(the_intervals([(3,5),(4,6)],[5]),'5 ∈ (4;6)')
        test.assert_equals(the_intervals([(1,50),(3,7)],[4,3]),'4 ∈ (1;50) ∩ (3;7) and 3 ∈ (1;50)')
        test.assert_equals(the_intervals([(2,7),(4,9)],[1,10]),'')
        test.assert_equals(the_intervals([(1,7),(2,8),(3,9)],[4,3,8]),'4 ∈ (1;7) ∩ (2;8) ∩ (3;9) and 3 ∈ (1;7) ∩ (2;8) and 8 ∈ (3;9)')