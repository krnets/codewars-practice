import codewars_test as test
from kata import grid_map

@test.describe("Fixed tests")
def test_group():
    
    num_grid = [[1,2,3,4], [5,6,7,8,9], [0,2,4]]
    char_grid = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]
    
    @test.it("Addition")
    def test_case1():
        test.assert_equals(grid_map(num_grid, lambda x: x + 1), 
                           [[2,3,4,5], [6,7,8,9,10], [1,3,5]])
    @test.it("Multiplication")
    def test_case2():
        test.assert_equals(grid_map(num_grid, lambda x: x * 2), 
                           [[2,4,6,8], [10,12,14,16,18], [0,4,8]])
    @test.it("Power")
    def test_case3():
        test.assert_equals(grid_map(num_grid, lambda x: x ** 2), 
                           [[1,4,9,16],[25,36,49,64,81],[0,4,16]])
    @test.it("Upper")
    def test_case4():
        test.assert_equals(grid_map(char_grid, lambda x: x.upper()), 
                           [['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']])
    @test.it("Lower")
    def test_case5():
        test.assert_equals(grid_map(char_grid, lambda x: x.lower()), 
                           [['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd']])