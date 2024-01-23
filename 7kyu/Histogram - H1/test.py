import codewars_test as test
from kata import histogram


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        res = """6|##### 5
5|
4|# 1
3|########## 10
2|### 3
1|####### 7
"""
        test.assert_equals(histogram([7, 3, 10, 1, 0, 5]), res)
        res = """6|
5|
4|
3|
2|
1|
"""
        test.assert_equals(histogram([0, 0, 0, 0, 0, 0]), res)
