import codewars_test as test
from kata import minimum_number

tests = {
    1: ([3,1,2], 1),
    2: ([5,2], 0),
    3: ([1,1,1], 0),
    4: ([2,12,8,4,6], 5),
    5: ([50, 39, 49, 6, 17, 28], 2)
}

@test.describe("Basic tests")
def test_group():
    @test.it('Simple Cases')
    def example_cases():
        for _, value in tests.items():
            test.assert_equals(minimum_number(value[0]), value[1], f"Incorrect result for {value[0]}")