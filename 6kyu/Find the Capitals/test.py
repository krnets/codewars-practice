import codewars_test as test
from kata import capital


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        state_capitals = [{"state": "Maine", "capital": "Augusta"}]
        test.assert_equals(capital(state_capitals), ["The capital of Maine is Augusta"])

        country_capitals = [{"country": "Spain", "capital": "Madrid"}]
        test.assert_equals(
            capital(country_capitals), ["The capital of Spain is Madrid"]
        )

        mixed_capitals = [
            {"state": "Maine", "capital": "Augusta"},
            {"country": "Spain", "capital": "Madrid"},
        ]
        test.assert_equals(
            capital(mixed_capitals),
            ["The capital of Maine is Augusta", "The capital of Spain is Madrid"],
        )
