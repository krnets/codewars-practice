import codewars_test as test
from kata import sort_by_area

@test.describe('Sort by area')
def example_tests():
    @test.it("Example tests")
    def examples():
        test.assert_equals(sort_by_area([ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ]), [ (1.342, 3.212), 1.23, (4.23, 6.43), 3.444 ] )
        test.assert_equals(sort_by_area([ (2, 5), 6 ]), [ (2, 5), 6 ])
        test.assert_equals(sort_by_area([]), [] )