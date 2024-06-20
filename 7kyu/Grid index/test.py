import codewars_test as test
from kata import grid_index

@test.describe("grid index")
def tests():
    @test.describe('Basic tests')
    def basic():
        results1 = grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        test.assert_equals(results1, 'myexample')
        results2 = grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 5, 6])
        test.assert_equals(results2, 'mam')
        results3 = grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 3, 7, 8])
        test.assert_equals(results3, 'mepl')
        results4 = grid_index([['h', 'e', 'l', 'l'], ['o', 'c', 'o', 'd'], ['e', 'w', 'a', 'r'], ['r', 'i', 'o', 'r']], [5, 7, 9, 3, 6, 6, 8, 8, 16, 13])
        test.assert_equals(results4, 'ooelccddrr')