import codewars_test as test
from kata import alan

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(alan(["Norwich", "Rejection", "Disappointment", "Backstabbing Central", "Shattered Dreams Parkway", "London"]), "Smell my cheese you mother!")
        test.assert_equals(alan(["London", "Norwich"]), "No, seriously, run. You will miss it.")
        test.assert_equals(alan(["Norwich", "Tooting", "Bank", "Rejection", "Disappointment", "Backstabbing Central", "Exeter", "Shattered Dreams Parkway", "Belgium","London"]), "Smell my cheese you mother!")
        test.assert_equals(alan(["London", "Norwich"]), "No, seriously, run. You will miss it.")
        test.assert_equals(alan(["London", "Shattered Dreams Parkway", "Backstabbing Central", "Disappointment", "Rejection", "Norwich"]), "Smell my cheese you mother!")
