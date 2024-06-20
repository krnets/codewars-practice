import codewars_test as test
from kata import sum_arrays

@test.describe('Fixed Tests')
def test_groups():
    @test.it('Basic Tests')
    def basic_tests():
        test.assert_equals(sum_arrays([3,2,9],[1,2]),[3,4,1])
        test.assert_equals(sum_arrays([4,7,3],[1,2,3]),[5,9,6])
        test.assert_equals(sum_arrays([1],[5,7,6]),[5,7,7])
        test.assert_equals(sum_arrays([-3,4,2],[3,4,4]),[2])
        test.assert_equals(sum_arrays([],[]),[])
        test.assert_equals(sum_arrays([0],[]),[0])
        test.assert_equals(sum_arrays([],[1,2]),[1,2])