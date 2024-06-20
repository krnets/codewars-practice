from kata import iter_pi
import codewars_test as test

@test.describe("Tests...")
def _():
    
    @test.it("Fixed tests")
    def _():
        test.assert_equals(iter_pi(0.1), [10, 3.0418396189])
        test.assert_equals(iter_pi(0.01), [100, 3.1315929036])
        test.assert_equals(iter_pi(0.001), [1000, 3.1405926538])
        