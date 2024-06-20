from kata import take_umbrella
import codewars_test as test


@test.describe("Umbrella decider")
def umbrella_decider():

    @test.it("Basic tests")
    def basic_tests():

        test.assert_equals(take_umbrella("sunny", 0.40), False)
        test.assert_equals(take_umbrella("rainy", 0.0), True)
        test.assert_equals(take_umbrella("cloudy", 0.20), False)
