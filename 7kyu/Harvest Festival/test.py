from kata import plant
import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(plant(",", 3, 7, 25), "---,,,,,,,---,,,,,,,---,,,,,,,")
        test.assert_equals(plant("+", 1, 3, 15), "-+")
        test.assert_equals(
            plant(";", 9, 10, 30),
            "---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;",
        )

        test.assert_equals(plant("@", 3, 3, 25), "---@@@---@@@---@@@")
        test.assert_equals(plant("$", 4, 2, 30), "----$$----$$----$$----$$")
        test.assert_equals(plant("&", 1, 5, 20), "-&&&&&")
        test.assert_equals(plant("^", 3, 3, 35), "---------^")