import codewars_test as test


def calculate_years(principal, interest, tax, desired):
    years = 0
    total = principal
    while total < desired:
        interest_accrued_in_year = total * interest
        interest_taxed_in_year = interest_accrued_in_year * tax
        total += interest_accrued_in_year
        total -= interest_taxed_in_year
        years += 1
    return years


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(calculate_years(1000, 0.05, 0.18, 1100), 3)
        test.assert_equals(calculate_years(1000, 0.01625, 0.18, 1200), 14)
        test.assert_equals(calculate_years(1000, 0.05, 0.18, 1000), 0)
