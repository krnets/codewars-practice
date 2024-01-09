import codewars_test as test
from kata import sentence


@test.describe("Fixed tests")
def fixed_tests():
    @test.it("Should pass fixed tests")
    def it():
        lst = [
            {"2": "took"},
            {"12": "spin"},
            {"5": "for"},
            {"4": "Vatsan"},
            {"1": "dog"},
            {"6": "a"},
        ]
        test.assert_equals(sentence(lst), "dog took Vatsan for a spin")

        lst = [
            {"1": "Forget"},
            {"2": "it"},
            {"3": "Jake."},
            {"4": "It is"},
            {"5": "Chinatown"},
        ]
        test.assert_equals(sentence(lst), "Forget it Jake. It is Chinatown")

        lst = [{"3": "vatsan!"}, {"2": "love"}, {"1": "I"}]
        test.assert_equals(sentence(lst), "I love vatsan!")

        lst = [{"0": "Wars"}, {"-1": "Code"}]
        test.assert_equals(sentence(lst), "Code Wars")
