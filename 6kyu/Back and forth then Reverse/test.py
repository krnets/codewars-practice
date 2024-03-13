import codewars_test as test
from kata import arrange

@test.describe("Fixed Test Cases")
def sample_tests():
    TESTS = [
        ([1,2], [1,2]),
        ([4, 3, 2], [4, 2, 3]),
        ([9, 7, -2, 8, 5, -3, 6, 5, 1], [9, 1, 5, 7, -2, 6, -3, 8, 5]),
        ([1], [1]),
        ([], []),
        ([2, 4, 3, 4],[2, 4, 3, 4]),
    ]
    for i,(inp,exp) in enumerate(TESTS,1):
        @test.it("test"+str(i))
        def test_1():
            inp2 = inp[:]
            test.assert_equals(arrange(inp), exp)
            test.assert_equals(inp, inp2, "Don't mutate the input")
    