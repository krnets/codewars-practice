import codewars_test as test
from kata import owned_cat_and_dog


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("should equal zero")
    def basic_test_cases():
        test.assert_equals(owned_cat_and_dog(9, 7), [0, 0])

    @test.it("should equal one")
    def basic_test_cases():
        test.assert_equals(owned_cat_and_dog(15, 15), [1, 1])
        test.assert_equals(owned_cat_and_dog(18, 21), [1, 1])
        test.assert_equals(owned_cat_and_dog(19, 17), [1, 1])

    @test.it("should equal two")
    def basic_test_cases():
        test.assert_equals(owned_cat_and_dog(24, 24), [2, 2])
        test.assert_equals(owned_cat_and_dog(25, 25), [2, 2])
        test.assert_equals(owned_cat_and_dog(26, 26), [2, 2])
        test.assert_equals(owned_cat_and_dog(27, 27), [2, 2])

    @test.it("should equal ten")
    def basic_test_cases():
        test.assert_equals(owned_cat_and_dog(56, 64), [10, 10])
