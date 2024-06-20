import codewars_test as test
from kata import correctness

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(correctness(('M', 'F', '?'), ('M', 'F', '?')), 3)
        test.assert_equals(correctness(('M', '?', 'M'), ('M', 'F', '?')), 2)
        test.assert_equals(correctness(('F', 'M', 'F'), ('M', 'F', 'M')), 0)