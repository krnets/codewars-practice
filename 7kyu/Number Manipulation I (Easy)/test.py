import codewars_test as test
from kata import manipulate

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(manipulate(192827764920), 192827000000)
        test.assert_equals(manipulate(838473), 838000)
        test.assert_equals(manipulate(8173648710293847), 8173648700000000)
        test.assert_equals(manipulate(283749202), 283700000)
        test.assert_equals(manipulate(1202), 1200)
        test.assert_equals(manipulate(422), 400)
        test.assert_equals(manipulate(30000000), 30000000)