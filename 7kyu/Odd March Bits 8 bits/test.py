import codewars_test as test
from kata import bit_march

@test.describe("Tests")
def tests():

    def do_test(n, expected):
        actual = bit_march(n)
        test.assert_equals(actual, expected, f'for n = {n}\n')

    @test.it("sample_tests")
    def sample_tests():
        do_test(2, [
            [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
        ])
        do_test(3, [
            [0, 0, 0, 0, 0, 1, 1, 1, ],
            [0, 0, 0, 0, 1, 1, 1, 0, ],
            [0, 0, 0, 1, 1, 1, 0, 0, ],
            [0, 0, 1, 1, 1, 0, 0, 0, ],
            [0, 1, 1, 1, 0, 0, 0, 0, ],
            [1, 1, 1, 0, 0, 0, 0, 0, ],
        ])