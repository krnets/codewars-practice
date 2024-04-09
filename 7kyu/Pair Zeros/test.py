import codewars_test as test
from kata import pair_zeros

@test.describe('Basic tests')
def _():
    @test.it('_empty array')
    def _():
        test.assert_equals(pair_zeros([]),[])
        
    @test.it('Without zeros [1] -> [1]')
    def _():
        test.assert_equals(pair_zeros([1]),[1])

    @test.it('Without zeros [1,2,3] -> [1,2,3]')
    def _():
        test.assert_equals(pair_zeros([1,2,3]),[1,2,3])

    @test.it('[0] -> [0]')
    def _():
        test.assert_equals(pair_zeros([0]),[0])
        
    @test.it('[0,0] -> [0]')
    def _():
        test.assert_equals(pair_zeros([0,0]),[0])
        
    @test.it('[1,0,1,0,2,0,0] -> [1,0,1,2,0]')
    def _():
        test.assert_equals(pair_zeros([1,0,1,0,2,0,0]),[1,0,1,2,0])
        
    @test.it('[0,0,0] -> [0,0]')
    def _():
        test.assert_equals(pair_zeros([0,0,0]),[0,0])
        
    
    @test.it('[1,0,1,0,2,0,0,3,0] -> [1,0,1,2,0,3,0]')
    def _():
        test.assert_equals(pair_zeros([1,0,1,0,2,0,0,3,0]),[1,0,1,2,0,3,0])
        
    @test.it('handles large arrays')
    def _():
        test.assert_equals(pair_zeros([0,0,0,0,0,0,0,0,0,0,0,0]),[0,0,0,0,0,0])
        test.assert_equals(pair_zeros([0,0,0,0,0,0,0,0,0,0,0,0,0]),[0,0,0,0,0,0,0])